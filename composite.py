from PIL import Image
import io
import cairosvg
import os
import utils


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
        parent_height=image.size[1],
        parent_width=image.size[0],
        write_to=f'/tmp/{svg_filename}.png'
    )

    # Create a PIL image from the PNG data
    svg_image = Image.open(f'/tmp/{svg_filename}.png', 'r',)

    # Create a new image by layering the original image and the SVG image
    result = Image.alpha_composite(image.convert("RGBA"), svg_image)

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
    # print(bg_filenames)
    svg_filenames = [
        file for file in os.listdir(svg_folder) if utils.is_svg_file(file)
    ]
    # each image
    for i in range(len(svg_filenames)):
        save_as_layered(
            svg_folder, svg_filenames[i], bg_folder, bg_filenames[i]
        )