import cv2

# Chapter 3 - Resizing and Cropping Images

if __name__ == '__main__':
    # read in image
    img = cv2.imread('static/kaaba.png')
    # show the dimensions of the image
    print(img.shape)
    # Resize the image - this adjusts the number of pixels
    img_resized = cv2.resize(img, (300, 200))

    # cropping images - pick how much of the original image's H and W you want
    img_cropped = img[0:200, 200:500]

    # show the images
    # cv2.imshow("Image", img)
    # cv2.imshow("Resized Image", img_resized)
    cv2.imshow("Cropped Image", img_cropped)
    cv2.waitKey(70000)
