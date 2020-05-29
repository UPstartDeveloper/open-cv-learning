import cv2
import numpy as np

# Joining images
# useful for when you are working with LOTS of images

'''
The  following function is copied from the website of Murtaza Hassan:
https://www.murtazahassan.com/learn-opencv-in-3-hours-chapter-6/
'''


def stack_images(scale, img_array):
    """
    This function handles joining images and offers two main improvements
    over the opencv built-in methods:
        1. Images can be resized
        2. Images do not need to have the same number of "channels"
            (either both being RGB, or both being black and white)

    Thanks to these improvements, the function is able to construct joined
    images in both the horizontal and vertical directions.

    """
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available is True:
        for x in range(rows):
            for y in range(cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y],
                                                 (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y],
                                                 (img_array[0][0].shape[1],
                                                 img_array[0][0].shape[0]),
                                                 None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y],
                                                   cv2.COLOR_GRAY2BGR)
        img_blank = np.zeros((height, width, 3), np.uint8)
        hor = [img_blank] * rows
        hor_con = [img_blank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x],
                                          (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1],
                                          img_array[0].shape[0]), None, scale,
                                          scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


if __name__ == '__main__':
    img = cv2.imread("static/mugshot.png")

    # create a horizontal stack
    # img_hor = np.hstack((img, img))
    # create a vertical stack
    # img_ver = np.vstack((img, img))

    # joining using the custom function above
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converts RBG to B&W
    img_stack = stack_images(0.5, ([img, img_gray, img],  # hor and ver stack
                                   [img, img, img]))  # must be square matrix

    # Show the images
    # cv2.imshow("Horizontal", img_hor)
    # cv2.imshow("Vertical", img_ver)
    cv2.imshow("Image Stack", img_stack)

    cv2.waitKey(100000)
