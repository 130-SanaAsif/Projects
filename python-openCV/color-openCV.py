import cv2

image_path = r'image.png.jpg'
image = cv2.imread(image_path)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#colour = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
cv2.imshow('Original Image', image)

cv2.imshow('Gray Image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()