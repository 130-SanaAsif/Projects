import cv2

image_path = r'image.png.jpg'
image = cv2.imread(image_path)

text = "Bubble Tea"
coordinates = (50,50)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
colour = (2500,900,29)
thick = 2

image = cv2.putText(image,text,coordinates,font,fontScale,colour,thick)
cv2.imshow('Sample Image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()