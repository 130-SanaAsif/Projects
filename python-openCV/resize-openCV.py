import cv2

image_path1 = r'photos/Cat.jpg'
image1 = cv2.imread(image_path1)
resize = cv2.resize(image1,(600,200))
cv2.imshow('Original Image', image1)
cv2.imshow('Resized Image', resize)

cv2.waitKey(0)
cv2.destroyAllWindows()