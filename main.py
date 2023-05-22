import os
import cv2
import shadow
import resize
import colorize
import composite
import blur
import brightness_adjust
import contrast
import noise
import utils
import finished_mask
import random


def process_all_in_dir(svg_path, bg_path):
    # get filenames
    svg_filenames = [file for file in os.listdir(
        svg_path) if utils.is_svg_file(file)]
    bg_filenames = [file for file in os.listdir(
        bg_path) if utils.is_image_file(file)]
    n = len(bg_filenames)
    svg_filenames = random.sample(svg_filenames, n)
    for i in range(n):
        svg_filename = svg_filenames[i]
        bg_filename = bg_filenames[i]
        svg = open(f'{svg_path}/{svg_filename}', 'r').read()
        img = cv2.imread(f'{bg_path}/{bg_filename}')
        process(img, svg, f'{svg_path}/{svg_filename}')


def process(img, svg, svg_path):
    img = resize.perform(img, 512)
    img = colorize.perform(
        img,
        utils.normal_num(0, 1),
        int(utils.normal_num(0, 255)),
        int(utils.normal_num(0, 255)),
        int(utils.normal_num(0, 255)),
    )
    img, raw_mask = composite.perform(svg, img, svg_path.split('/')[-1])
    img = shadow.perform(img)
    k = 0
    while (k % 2 != 1):
        k = int(utils.normal_num(1, 13))
    img = blur.perform(img, k)
    alpha = utils.normal_num(0.4, 1.9)
    img = brightness_adjust.perform(img, alpha)
    # alpha = utils.normal_num(0.4, 1.9)
    # img = contrast.perform(img, 1)
    g_mean = utils.normal_num(1.6, 2.6)
    sp_prob = utils.normal_num(0.002, 0.03)
    img = noise.perform(img, g_mean, sp_prob)

    mask = finished_mask.extract(img, raw_mask)

    svg_filename = svg_path.split('/')[-1]
    mask.save(f'assets/train/masks/{svg_filename}.png')
    cv2.imwrite(f'assets/train/samples/{svg_filename}.png', img)


def main():
    # make output folder if not exists
    os.makedirs("assets/train/masks", exist_ok=True)
    os.makedirs("assets/train/samples", exist_ok=True)

    # processing
    process_all_in_dir('assets/svg', 'assets/patterns')


if __name__ == "__main__":
    main()
