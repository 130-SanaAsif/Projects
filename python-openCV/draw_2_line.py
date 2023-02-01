import numpy as np
import cv2

path = np.zeros((512,512,3),dtype='uint8')
start_point = (100,100)
end_point = (450,450)
thick = 4
colour = (250,250,250)

image = cv2.line(path,start_point,end_point,colour,thick)
cv2.imshow('Sample Image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()