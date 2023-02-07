import cv2

path = r'image.png.jpg'
image = cv2.imread(path)

start = 0
end = 360
thick = -10
colour = (255,0,255)
center_coordinates = (120,100)
axislength = (100,50)
angle = 30

ellip = cv2.ellipse(image, center_coordinates,axislength, angle, start, end, colour, thick)
cv2.imshow('Sample Image', ellip)

cv2.waitKey(0)
cv2.destroyAllWindows()