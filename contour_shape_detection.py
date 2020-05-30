import cv2
import numpy as np
from joining_images import stack_images

# Chapter 8 - Contour and Shape Detection


def get_contours(image):
    '''Find the contours in an image.'''
    # cv2.findContours requires args for the following:
    # 1. the image being analyzed
    # 2. retriever method - in this case we'll be getting the outermost corners
    contours, hierarchy = cv2.findContours(img,
                                           cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    # find the area of each edge
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)


if __name__ == '__main__':
    # read in the image
    path = 'static/shapes.png'
    img = cv2.imread(path)

    # preprocessing - convert to gray scale and blurred copies
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)

    # detect the contours using the edge detector
    img_canny = cv2.Canny(img_blur, 50, 50)

    # just demoing - we can create "blank" images as well
    get_contours(img_gray)
    img_blank = np.zeros_like(img)

    # show the images
    img_stack = stack_images(0.3, ([img, img_gray, img_blur],
                                   [img_canny, img_blank, img_blank]))
    cv2.imshow("Images", img_stack)
    cv2.waitKey(100000)
