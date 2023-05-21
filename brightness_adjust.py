import utils
import cv2
import numpy as np
import os


def save_as_brightness_adjusted(path, filename, alpha=1.5):
    # Load the image
    image = cv2.imread(f'{path}/{filename}')

    # Adjust the exposure/brightness
    adjusted_image = np.clip(image * alpha, 0, 255).astype(np.uint8)

    # Save the adjusted image
    output_path = f"{path}/../brightness_adjusted/{filename}"
    cv2.imwrite(output_path, adjusted_image)


def brightness_adjust_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../brightness_adjusted", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(
        folder_name) if utils.is_image_file(file)]
    n = len(filenames)
    # get a range of alphas that correspond to standard distribution
    # alphas: 0.4 to 1.9
    alphas = utils.st_dist(n, min=0.4, max=1.9, dec=1)
    for i, filename in enumerate(filenames):
        save_as_brightness_adjusted(folder_name, filename, alphas[i])