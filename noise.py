import cv2
import numpy as np
import os
import utils

def perform(img, g_mean,sp_prob):
    """gaussian mean: 1.6 - 2.6, salt-pepper prob: 0.002-0.03"""
    img = utils.correct_img_type(img,'cv2')
    # Add Gaussian noise
    std_dev = 1
    gaussian_noise = np.random.normal(
        g_mean, std_dev, img.shape).astype(np.uint8)
    img = cv2.add(img, gaussian_noise)

    # Add salt and pepper noise
    salt_pepper_mask = np.random.rand(*img.shape[:2])
    salt_mask = salt_pepper_mask < sp_prob / 2
    pepper_mask = salt_pepper_mask > 1 - sp_prob / 2
    img[salt_mask] = 255
    img[pepper_mask] = 0
    
    return img
