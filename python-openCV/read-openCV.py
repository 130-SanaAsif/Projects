import cv2

image_path = r'image.png.jpg'
image = cv2.imread(image_path)
cv2.imshow('Sample Image',image)

cv2.waitKey(0)
cv2.destroyAllWindows()

directory = r'Downloads'
cv2.imwrite('365_DataScience.png',image)
print("Image was succesfully saved")

print(image.shape)