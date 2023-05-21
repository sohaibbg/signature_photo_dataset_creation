import cv2
import numpy as np
import os
import utils


def save_as_noised(path, filename, g_mean=2.6, sp_prob=0.002):
    # Load the image
    image = cv2.imread(f"{path}/{filename}")

    # Add Gaussian noise
    std_dev = 1
    gaussian_noise = np.random.normal(
        g_mean, std_dev, image.shape).astype(np.uint8)
    image = cv2.add(image, gaussian_noise)

    # Add salt and pepper noise
    salt_pepper_mask = np.random.rand(*image.shape[:2])
    salt_mask = salt_pepper_mask < sp_prob / 2
    pepper_mask = salt_pepper_mask > 1 - sp_prob / 2
    image[salt_mask] = 255
    image[pepper_mask] = 0

    # save the noisy images
    cv2.imwrite(f"{path}/../noised/{filename}", image)

def noise_all_in_dir(folder_name):
    # make output folder if not exists
    os.makedirs(f"{folder_name}/../noised", exist_ok=True)
    # get filenames
    filenames = [file for file in os.listdir(folder_name) if utils.is_image_file(file)]
    n = len(filenames)
    # get a range of noise props that correspond to standard distribution
    # gaussian mean: 1.6 - 2.6
    g_means = utils.st_dist(n, min=1.6, max=2.6, dec=1)
    # salt-pepper prob: 0.002-0.03
    sp_probs = utils.st_dist(n, min=0.002, max=0.03, dec=3)
    for i, filename in enumerate(filenames):
        save_as_noised(folder_name,filename,g_means[i],sp_probs[i])