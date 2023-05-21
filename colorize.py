import os
from PIL import Image
import utils
import random


def save_as_colorized(path, filename):
    # Open the PNG image
    image = Image.open(f"{path}/{filename}")

    for i in range(30):
        # create the random properties
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        a = random.randint(0, 255)

        # Create the shaded images
        green_shade = Image.new("RGB", image.size, color=(r, g, b))

        # Blend the green shade with the original image
        blended_image = Image.blend(image, green_shade, alpha=a)

        # Save the resulting image
        output_path = f"{path}/../colorized/{i}-{filename}"
        blended_image.save(output_path)


def colorize_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../colorized", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(
        folder_name) if utils.is_image_file(file)]
    n = len(filenames)
    # each image
    for i, filename in enumerate(filenames):
        save_as_colorized(folder_name, filename)
