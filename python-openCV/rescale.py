import cv2 as cv
def rescaleFrame(frame, scale=0.95):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("videos/cat.mp4")
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow("Videos",frame)
    cv.imshow("Resized_videos",frame_resized)

    if cv.waitKey(20) & 0xff == ord('d'):
        break
capture.release()
cv.destroyAllWindows()

