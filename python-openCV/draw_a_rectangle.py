import cv2

path = r'image.png.jpg'
image = cv2.imread(path)

start_point = (100,50)
end_point = (20,100)
colour = (255,0,255)
thick = -5

rect = cv2.rectangle(image,start_point, end_point, colour, thick)
cv2.imshow('Sampple Image', rect)

cv2.waitKey(0)
cv2.destroyAllWindows
