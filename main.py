from shadow import shadow_all_in_dir
from resize import resize_all_in_dir
from colorize import colorize_all_in_dir
from composite import composite_all_in_dirs
from blur import blur_all_in_dir
from brightness_adjust import brightness_adjust_all_in_dir
from contrast import contrast_all_in_dir
from noise import noise_all_in_dir


def main():
    resize_all_in_dir('assets/patterns/original')
    colorize_all_in_dir('assets/patterns/resized')
    composite_all_in_dirs('assets/svg','assets/patterns/colorized')
    shadow_all_in_dir('assets/composited')
    blur_all_in_dir('assets/shadowed')
    brightness_adjust_all_in_dir('assets/blurred')
    contrast_all_in_dir('assets/brightness_adjusted')
    noise_all_in_dir('assets/contrasted')


if __name__ == "__main__":
    main()
