"""
File: blur.py
Name: Ester
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_p = new_img.get_pixel(x, y)
            if x == 0:
                r_1 = x
            else:
                r_1 = x - 1
            if x == (img.width - 1):
                r_n = x
            else:
                r_n = x + 1
            if y == 0:
                c_1 = y
            else:
                c_1 = y - 1
            if y == (img.height - 1):
                c_n = y
            else:
                c_n = y + 1

            total_red = 0
            total_blue = 0
            total_green = 0
            counts = 0
            for r in range(r_1, r_n + 1):
                for c in range(c_1, c_n + 1):
                    total_red += img.get_pixel(r, c).red
                    total_blue += img.get_pixel(r, c).blue
                    total_green += img.get_pixel(r, c).green
                    counts += 1

            new_p.red = total_red / counts
            new_p.blue = total_blue / counts
            new_p.green = total_green / counts
    return new_img


def main():
    """
    This file shows the original image first, smiley-face.png, and then compare to its blurred image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
