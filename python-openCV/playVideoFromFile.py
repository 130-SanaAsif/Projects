import cv2

cap = cv2.VideoCapture("videos/Capture_Video.mp4")
while True:
    isTrue,frame = cap.read()
    cv2.imshow("video",frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()