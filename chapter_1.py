import cv2


if __name__ == '__main__':
    """
    print("Package imported")
    # reading in an image file
    img = cv2.imread('static/mugshot.png')
    # showing an image
    cv2.imshow("Output", img)
    # delaying the amount of time the image stays
    cv2.waitKey(7000)
    """

    """
    # reading in a video file
    cap = cv2.VideoCapture('static/forest.mov')
    # display the video
    while True:
        # read in one image frame from thr video at a time
        sucess, img = cap.read()
        cv2.imshow("Video", img)
        # event-driven loop early exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    """

    # use the webcam for video
    cam = cv2.VideoCapture(0)
    # set the dimensions of the video to take
    cam.set(3, 640)  # 3 is for the width
    cam.set(4, 480)  # 4 is for the height
    cam.set(10, 100)  # 10 is for brightness settings

    # display the video from the camera - same as before
    while True:
        # read in one image frame from thr video at a time
        sucess, img = cam.read()
        cv2.imshow("Video", img)
        # event-driven loop early exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
