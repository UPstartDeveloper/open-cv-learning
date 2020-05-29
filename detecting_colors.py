import cv2
import numpy as np
from chapter_6 import stack_images

# Chapter 7 - Color Detection

if __name__ == '__main__':
    # creating 'trackbars' to see the optimal values for the color detection
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    '''
    These trackbars will look for the min/max numbers for:
    - the Hue
    - the Saturation
    - the value
    of the color we are tracking
    '''
    cv2.createTrackbar("Hue Min", "TrackBars", 44, 179, lambda x: x)
    cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, lambda x: x)
    cv2.createTrackbar("Sat Min", "TrackBars", 78, 255, lambda x: x)
    cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, lambda x: x)
    cv2.createTrackbar("Value Min", "TrackBars", 58, 255, lambda x: x)
    cv2.createTrackbar("Value Max", "TrackBars", 255, 255, lambda x: x)

    # figure out the values for the color being detected
    while True:  # you will need to MANUALLY exit out of this loop!
        # Read in the Image
        img = cv2.imread('static/mugshot.png')
        # convert the image to HSV space
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # make use of the trackbars above
        hue_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        hue_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        sat_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        sat_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        val_min = cv2.getTrackbarPos("Value Min", "TrackBars")
        val_max = cv2.getTrackbarPos("Value Max", "TrackBars")
        # capture these values in the terminal - the colors you want should
        # be white!
        print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)
        # create a 'mask' to adjust these values in the image
        lower, upper = (
            np.array([hue_min, sat_min, val_min]),
            np.array([hue_max, sat_max, val_max])
        )
        mask = cv2.inRange(img_HSV, lower, upper)
        # highltight the newly detected colors in the oriignal image!
        img_result = cv2.bitwise_and(img, img, mask=mask)
        # Showing images altogether
        img_stack = stack_images(0.6, (
            [img, img_HSV], [mask, img_result]
        ))
        cv2.imshow("Image Color Analysis", img_stack)
        cv2.waitKey(10000)
