import os
import utils
from PIL import Image
import cv2


def perform(img, new_height):
    img = utils.correct_img_type(img, 'cv2')
    # Calculate the corresponding width based on the aspect ratio
    height, width, _ = img.shape
    aspect_ratio = width / height
    desired_width = int(new_height * aspect_ratio)

    # Resize the image using cv2.resize()
    resized_img = cv2.resize(img, (desired_width, new_height))
    return resized_img