import utils
import cv2
import numpy as np
import os


def perform(img, alpha):
    """alpha 0.4 to 1.9"""
    img = utils.correct_img_type(img, 'cv2')

    # Adjust the exposure/brightness
    return np.clip(img * alpha, 0, 255).astype(np.uint8)