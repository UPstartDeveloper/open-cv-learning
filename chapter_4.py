import cv2
import numpy as np

# How to Draw Shapes and Text on Images

if __name__ == '__main__':
    # define an "image" only a matrix
    img = np.zeros((512, 512, 3), np.uint8)
    # print(img)  # print the numbers making up the "image" in CLI

    # "Color" the whole image, by manipulating the matrix values
    # img[:] = 255, 0, 0  # completely blue, darkly shaded
    # img[20:30, 10:30] = 255, 0, 0  # only a portion becomes dark blue
    print(img)

    # show the images
    cv2.imshow("Image", img)
    cv2.waitKey(100000)
