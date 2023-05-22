import os
import cv2
import utils
import random



def perform(img, k_size):
    """k_size must be odd, 1-13"""
    img = utils.correct_img_type(img, 'cv2')
    
    # Apply blur to the image
    return cv2.GaussianBlur(img, (k_size, k_size), sigmaX=0)