import os
import utils
from PIL import Image


def resize_img(path, filename, new_height=300):
    # Load the image
    image = Image.open(f'{path}/{filename}')

    # Calculate the new width while maintaining the aspect ratio
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    new_width = int(new_height * aspect_ratio)

    # Resize the image with the new width and height
    resized_image = image.resize((new_width, new_height))
    # Save the resized image
    output_path = f"{path}/../resized/{filename}"
    resized_image.save(output_path)


def resize_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../resized", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(
        folder_name) if utils.is_image_file(file)]
    n = len(filenames)
    heights = utils.st_dist(n, min=200, max=500, dec=0)
    for i, filename in enumerate(filenames):
        resize_img(
            folder_name,
            filename,
            new_height=int(heights[i])
        )