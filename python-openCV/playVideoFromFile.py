import cv2

cap = cv2.VideoCapture("Capture_Video.mp4")
while(True):
    ret_,frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()