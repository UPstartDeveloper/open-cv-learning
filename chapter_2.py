import cv2

'''Basic Function Everyone Should Know'''


if __name__ == '__main__':
    # read i =n the image
    img = cv2.imread('static/mugshot.png')
    # convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blur the image - asks for a value for the param kernelSize
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    # use of an edge detector - param valyes are for the threshold
    img_canny = cv2.Canny(img, 100, 100)
    # show the images
    # cv2.imshow("Gray Image", img_gray)
    # cv2.imshow("Blurred Image", img_gray)
    cv2.imshow("Image w/ Only Edges", img_canny)
    cv2.waitKey(10000)
