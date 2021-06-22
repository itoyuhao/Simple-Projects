"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return mirror_img: SimpleImage, the mirrored image with a upside-down mountain
    """
    # SimpleImage of the original image
    img = SimpleImage(filename)

    # Set a blank SimpleImage which is the same width and twice the height of the same image
    mirror_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            # Pixel of the original image
            pixel = img.get_pixel(x, y)

            # The upper half (the pixel of the position)
            upper = mirror_img.get_pixel(x, y)

            # The lower half (the pixel of the position)
            lower = mirror_img.get_pixel(x, mirror_img.height - 1 - y)

            # Fill pixel into the upper half of the blank image
            upper.red = pixel.red
            upper.green = pixel.green
            upper.blue = pixel.blue

            # Fill pixel into the lower half of the blank image
            lower.red = pixel.red
            lower.green = pixel.green
            lower.blue = pixel.blue

    return mirror_img


def main():
    """
    With using simpleimage.py, Output the original image and the mirrored image
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
