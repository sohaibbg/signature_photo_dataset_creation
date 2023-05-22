import os
from PIL import Image
import utils
import random
import numpy as np
import cv2

def perform(img, a, r, g, b):
    """a is 0-1, r,g,b 0-255"""
    img = utils.correct_img_type(img, 'PIL')

    # Create the shade
    shade = Image.new("RGB", img.size, color=(r, g, b))

    # Blend the shade with the original image
    img = Image.blend(img, shade, alpha=a)

    return img