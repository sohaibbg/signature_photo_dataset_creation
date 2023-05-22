import os
import cv2
import utils


def perform(img, alpha):
    """alphas 0.5 to 1.8"""
    img = utils.correct_img_type(img, 'cv2')

    # Adjust the contrast
    return cv2.convertScaleAbs(img, alpha=alpha)