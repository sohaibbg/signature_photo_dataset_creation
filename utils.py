import numpy as np
import os


def st_dist(n, min=0, max=1, dec=0):
    print('generating standard distribution')
    mean = (min + max)/2
    std_dev = (max - min)/4
    # Generate the list of numbers
    numbers = np.random.normal(mean, std_dev, n)
    numbers = np.clip(numbers, min, max)

    # Convert the numbers to decimals
    numbers = np.round(numbers, decimals=dec)
    return numbers

# Function to check if a file has an image extension


def is_image_file(file_name):
    image_extensions = [".jpg", ".jpeg", ".png", ".gif",
                        ".bmp", ".webp"]  # Add more extensions if needed
    _, extension = os.path.splitext(file_name)
    return extension.lower() in image_extensions

# Function to check if a file has an svg extension


def is_svg_file(file_name):
    _, extension = os.path.splitext(file_name)
    return extension.lower() in ".svg"
