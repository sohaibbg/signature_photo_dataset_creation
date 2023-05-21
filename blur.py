import os
import cv2
import utils
import random


def save_as_blurred(path, filename):
    # Load the image
    image = cv2.imread(f'{path}/{filename}')

    k_size = random.randint(1, 13)
    while (k_size % 2 == 0):
        k_size = random.randint(1, 13)
    # Apply blur to the image
    blurred_image = cv2.GaussianBlur(image, (k_size, k_size), sigmaX=0)

    # Save the blurred image
    output_path = f"{path}/../blurred/{filename}"
    cv2.imwrite(output_path, blurred_image)


def blur_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../blurred", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(
        folder_name) if utils.is_image_file(file)]
    n = len(filenames)
    for i, filename in enumerate(filenames):
        save_as_blurred(folder_name, filename)
