import cv2

cap = cv2.VideoCapture(0)

if(cap.isOpened == False):
    print("Camera could not capture video.")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

video_cod = cv2.VideoWriter_fourcc(*"XVID")
video_op = cv2.VideoWriter("Capture_Video.mp4", video_cod, 30, (frame_width, frame_height))

while(True):
    ret_,frame = cap.read()
    if ret_ == True:
        video_op.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
video_op.release()
cv2.destroyAllWindows()