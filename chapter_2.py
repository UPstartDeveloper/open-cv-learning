import cv2

'''Basic Function Everyone Should Know'''


if __name__ == '__main__':
    # read i =n the image
    img = cv2.imread('static/mugshot.png')
    # convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # show the image
    cv2.imshow("Gray Image", img_gray)
    cv2.waitKey(7000)
