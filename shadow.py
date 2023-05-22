import os
import utils
from PIL import Image, ImageDraw
import random


def perform(img):
    img = utils.correct_img_type(img, 'PIL')

    # Create a transparent layer for shadows
    shadow_image = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(shadow_image)

    n = int(utils.normal_num(0, 3))
    # number of shadows
    for _ in range(n):
        # shape has upto 5 sides
        sides = int(utils.normal_num(3, 5))
        shadow_shape = []
        # add points
        for i in range(sides):
            shadow_shape.append((
                random.uniform(0, img.width),
                random.uniform(0, img.height),
            ))
        # opacity between 0 (transparent) and 255 (opaque)
        shadow_color = (
            random.randint(0, 170),
            random.randint(100, 255),
            random.randint(0, 170),
            random.randint(30, 170)
        )

        # Draw the shadow shape on the shadow image
        draw.polygon(shadow_shape, fill=shadow_color, width=1000)

    # Blend the shadow image with the original image
    result = Image.alpha_composite(img.convert("RGBA"), shadow_image)
    return result