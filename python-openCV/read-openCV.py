import cv2

image_path = r'photos/cat.jpg'
image = cv2.imread(image_path)
cv2.imshow('Cat',image)

cv2.waitKey(0)
cv2.destroyAllWindows()

directory = r'Downloads'
cv2.imwrite('365_DataScience.png',image)
print("Image was succesfully saved")

print(image.shape)