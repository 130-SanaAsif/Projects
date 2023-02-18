import cv2
# 1 for colour picture GRAY->RGB.
# 0 for gray colour RGB->GRAY.
# -1 this keeps the image as it is.
image = cv2.imread("flower.jpg",0)
cv2.imshow("Original image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()