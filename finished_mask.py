import utils
from PIL import Image, ImageOps


def extract(img, raw_mask):
    # img = utils.correct_img_type(img, 'PIL')
    raw_mask = utils.correct_img_type(raw_mask, 'PIL')
    # Invert the transparency of the mask
    # inverted_mask = Image.new("RGBA", raw_mask.size)
    width, height = raw_mask.size

    for y in range(height):
        for x in range(width):
            r, g, b, a = raw_mask.getpixel((x, y))
            if a == 255:
                raw_mask.putpixel((x, y), (255, 255, 255, 255))
            else:
                raw_mask.putpixel((x, y), (0, 0, 0, 255))
    return raw_mask
    utils.display_img(raw_mask)
    result = Image.new("RGBA", img.size)
    result.paste(img, (0, 0))
    result = Image.alpha_composite(result, inverted_mask)
    return result

    raw_mask = raw_mask.convert("RGBA")
    result = Image.new("RGBA", raw_mask.size)

    utils.display_img(raw_mask)
    # Iterate over each pixel in img
    for x in range(raw_mask.width):
        for y in range(raw_mask.height):
            # Get the pixel value at (x, y) from 'image1'
            pixel1 = raw_mask.getpixel((x, y))

            # Extract the alpha value from the pixel
            alpha = pixel1[3]

            if alpha > 0:
                # Get the corresponding pixel value from 'img'
                pixel2 = img.getpixel((x, y))

                # Update the pixel value in the result image
                result.putpixel((x, y), pixel2)
    return result
