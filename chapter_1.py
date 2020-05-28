import cv2


if __name__ == '__main__':
    print("Package imported")

    # reading in an image file
    img = cv2.imread('static/mugshot.png')
    # showing an image
    cv2.imshow("Output", img)
    # delaying the amount of time the image stays
    cv2.waitKey(7000)
