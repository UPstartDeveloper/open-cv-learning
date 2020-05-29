import cv2
import numpy as np

# Chapter 4 - How to Draw Shapes and Text on Images

if __name__ == '__main__':
    # define an "image" only a matrix
    img = np.zeros((512, 512, 3), np.uint8)
    # print(img)  # print the numbers making up the "image" in CLI

    # "Color" the whole image, by manipulating the matrix values
    # img[:] = 255, 0, 0  # completely blue, darkly shaded
    # img[20:30, 10:30] = 255, 0, 0  # only a portion becomes dark blue
    # print(img)

    '''
    Drawing a Line on the image
    Args:
    - the image being drawn on
    - starting point of the line
    - the ending point
    - the color of the line
    - the thickness of the line
    '''
    # cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
    # Example where the line goes all the way across (so dimensions are used)
    # cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

    '''
    Drawing a Rectangle on the image
    Args (roughly the same convention):
    - image
    - the endpoints (for top-left to bottom-right diagonal)
    - color
    - thickness (or, you can put cv2.FILLED to color in the rectangle)
    '''
    # cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

    '''
    Drawing a Circle on the image
    Args (roughly the same convention):
    - image
    - coordinates of the center of the circle
    - radius length
    - color of the outline
    - thickness (or can be filled in)
    '''
    # cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

    '''
    Adding text to images
    Args
    - image
    - text that will be shown
    - starting coordinates for where the text will be shown
    - the font of the text
    - scale (think of it like font size)
    - color
    - thickness (like the "boldness" of the text)
    '''
    cv2.putText(img,
                "AI is so cool!",
                (112, 200),
                cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 130, 0), 1)

    # show the images
    cv2.imshow("Image", img)
    cv2.waitKey(100000)
