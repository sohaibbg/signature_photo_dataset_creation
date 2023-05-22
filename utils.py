import random
import numpy as np
import os
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np


def display_img(img):
    if isinstance(img, Image.Image):
        img.show()
    else:
        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


def correct_img_type(img, type):
    if type == 'PIL':
        if isinstance(img, np.ndarray) and len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
    elif type == 'cv2':
        if isinstance(img, Image.Image):
            img = np.array(img)
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)
    return img


def normal_num(min, max):
    sigma = (max-min)/2.5
    mu = (max+min)/2
    x = max+1
    while (x > max or x < min):
        x = random.normalvariate(mu, sigma)
    return x


if __name__ == '__main__':
    x = []
    for i in range(100):
        x.append(round(normal_num(0, 1), 2))
    x.sort()
    plt.hist(x, bins='auto')
    plt.show()


def is_image_file(file_name):
    """Function to check if a file has an image extension"""
    image_extensions = [".jpg", ".jpeg", ".png", ".gif",
                        ".bmp", ".webp"]  # Add more extensions if needed
    _, extension = os.path.splitext(file_name)
    return extension.lower() in image_extensions


def is_svg_file(file_name):
    """Function to check if a file has an svg extension"""
    _, extension = os.path.splitext(file_name)
    return extension.lower() in ".svg"
