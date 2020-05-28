import cv2


if __name__ == '__main__':
    print("Package imported")

    # reading in an image file
    img = cv2.imread('jerusalem.jpg')

    # showing an image
    cv2.imshow("Output", img)
