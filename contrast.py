import os
import cv2
import utils


def save_as_contrasted(path, filename, alpha=1.5, beta=1.5):
    # Load the image
    image = cv2.imread(f'{path}/{filename}')

    # Adjust the contrast
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Save the adjusted image
    output_path = f"{path}/../contrasted/{filename}"
    cv2.imwrite(output_path, adjusted_image)


def contrast_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../contrasted", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(
        folder_name) if utils.is_image_file(file)]
    n = len(filenames)
    # get a range of alphas that correspond to standard distribution
    # alphas: -0.8 to 1.8
    alphas = utils.st_dist(n, min=0.5, max=1.8, dec=1)
    betas = utils.st_dist(n, min=-0.5, max=1.8, dec=1)
    for i, filename in enumerate(filenames):
        save_as_contrasted(folder_name, filename, alphas[i], betas[i])


contrast_all_in_dir("assets/patterns/original")
