import cv2


if __name__ == '__main__':
    print("Package imported")

    """
    # reading in an image file
    img = cv2.imread('static/mugshot.png')
    # showing an image
    cv2.imshow("Output", img)
    # delaying the amount of time the image stays
    cv2.waitKey(7000)
    """

    # reading in a video file
    cap = cv2.VideoCapture('static/forest.mov')
    # display the video
    while True:
        # read in one image frame from thr video at a time
        sucess, img = cap.read()
        cv2.imshow("Video", img)
        # event-driven loop exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
