import cv2
import numpy as np

# Warp Perspective

if __name__ == '__main__':
    img = cv2.imread("static/mugshot.png")

    # define four points for your perspective
    points_1 = np.float32([
        [138, 32],  # each point needs (x, y) coordinates,
        [465, 46],
        [138, 550],
        [465, 550]
    ])
    # the key here is you ALSO need to define the points that the ones above^
    # are located in REFERENCE too! e.g. the first point is usually
    # in near the origin
    width, height = 668, 670
    points_2 = np.float32([
        [0, 0],
        [width, 0],
        [0, height],
        [width, height]
    ])

    # transform the perspective now
    matrix = cv2.getPerspectiveTransform(points_1, points_2)
    img_output = cv2.warpPerspective(img, matrix, (width, height))

    # Show the images
    # cv2.imshow("Image", img)
    cv2.imshow("Output of Warp", img_output)
    cv2.waitKey(10000)
