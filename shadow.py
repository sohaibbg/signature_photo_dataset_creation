import os
import utils
from PIL import Image, ImageDraw
import random


def save_as_shadowed(path, filename):
    # Load the image
    image = Image.open(f'{path}/{filename}')

    # Create a transparent layer for shadows
    shadow_image = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow_image)

    # choose between 0 and 5 shadows
    num_shadows = int(random.uniform(0, 5))

    for _ in range(num_shadows):
        # shape has upto 6 sides
        sides = int(random.uniform(3, 6))
        shadow_shape = []
        # add points
        for i in range(sides):
            shadow_shape.append((
                random.uniform(0, image.width),
                random.uniform(0, image.height),
            ))
        # opacity between 0 (transparent) and 255 (opaque)
        shadow_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(30,180)
        )

        # Draw the shadow shape on the shadow image
        draw.polygon(shadow_shape, fill=shadow_color, width=1000)

    # Blend the shadow image with the original image
    result = Image.alpha_composite(image.convert("RGBA"), shadow_image)

    # Save the result
    output_path = f"{path}/../shadowed/{filename}"
    result.save(output_path)


def shadow_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../shadowed", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(
        folder_name) if utils.is_image_file(file)]
    for filename in filenames:
        save_as_shadowed(folder_name, filename)