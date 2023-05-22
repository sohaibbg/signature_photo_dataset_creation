from PIL import Image
import cairosvg
import os
import utils
import random


def perform(svg, bg_img, svg_filename):
    """svg format should be: svg = open(svg_img_path, 'r').read()"""
    bg_img = utils.correct_img_type(bg_img, 'PIL')
    # write svg2png file
    cairosvg.svg2png(
        bytestring=svg,
        parent_height=256,
        parent_width=256,
        write_to=f'/tmp/{svg_filename}.png'
    )
    # create PIL img for svg
    svg_img = Image.open(f'/tmp/{svg_filename}.png', 'r',)
    # Calculate svg position on img as centered
    x = (bg_img.width - svg_img.width) // 2
    y = (bg_img.height - svg_img.height) // 2

    # get mask with proper dimensions
    result = Image.new("RGBA", bg_img.size, (0, 0, 0, 0))
    # paste svg in center
    result.paste(svg_img, (x, y))
    # save
    result.save(f'/tmp/{svg_filename}.png')
    raw_mask = result
    # reset canvas
    result = Image.new("RGBA", bg_img.size, (0, 0, 0, 0))

    # layer on canvas
    result.paste(bg_img, (0, 0))
    result.paste(svg_img, (x, y), mask=svg_img)

    return (result, raw_mask)


def save_as_layered(svg_path, svg_filename, bg_path, bg_filename):
    # Load the image
    image_path = f"{bg_path}/{bg_filename}"
    image = Image.open(image_path)

    # Load the SVG
    svg_img_path = f"{svg_path}/{svg_filename}"
    svg_data = open(svg_img_path, 'r').read()

    # Convert the SVG to a PNG image
    cairosvg.svg2png(
        bytestring=svg_data,
        parent_height=256,
        parent_width=256,
        write_to=f'/tmp/{svg_filename}.png'
    )

    # Create a PIL image from the PNG data
    svg_image = Image.open(f'/tmp/{svg_filename}.png', 'r',)

    # Create a new image with transparent background
    result = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Calculate the position to center the SVG on the image
    x = (image.width - svg_image.width) // 2
    y = (image.height - svg_image.height) // 2

    # Paste the image and SVG onto the result image
    result.paste(image, (0, 0))
    result.paste(svg_image, (x, y), mask=svg_image)
    # # Create a new image by layering the original image and the SVG image
    #     result = Image.alpha_composite(image.convert("RGBA"), svg_image)

    # Save the result
    output_path = f"{svg_path}/../composited/{svg_filename}_on_{bg_filename}"
    result.save(output_path)


def composite_all_in_dirs(svg_folder, bg_folder):
    # make output folder if not exists
    os.makedirs(f"{svg_folder}/../composited", exist_ok=True)
    # get filenames
    bg_filenames = [
        file for file in os.listdir(bg_folder) if utils.is_image_file(file)
    ]
    bg_filenames = random.sample(bg_filenames, 300)
    svg_filenames = [
        file for file in os.listdir(svg_folder) if utils.is_svg_file(file)
    ]
    svg_filenames = random.sample(svg_filenames, 300)
    # each image
    for i in range(len(svg_filenames)):
        save_as_layered(
            svg_folder, svg_filenames[i], bg_folder, bg_filenames[i]
        )
