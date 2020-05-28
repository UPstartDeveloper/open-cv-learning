import cv2
import numpy as np

'''Basic Function Everyone Should Know'''


if __name__ == '__main__':
    # read i =n the image
    img = cv2.imread('static/mugshot.png')
    # convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur the image - asks for a value for the param kernelSize
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    # use of an edge detector - param values are for the threshold
    img_canny = cv2.Canny(img, 100, 100)
    # image dilation - increases the thickness of edges
    # kernel matrix defined using Numpy
    kernel = np.ones((5, 5), np.uint8)
    img_dialation = cv2.dilate(img_canny, kernel, iterations=1)
    # image errosion - making the image "thinner"
    img_eroded = cv2.erode(img_dialation, kernel, iterations=1)
    # show the images
    # cv2.imshow("Gray Image", img_gray)
    # cv2.imshow("Blurred Image", img_gray)
    # cv2.imshow("Image w/ Only Edges", img_canny)
    cv2.imshow("Dialated Image", img_dialation)
    cv2.imshow("Eroded Image", img_eroded)
    cv2.waitKey(10000)
