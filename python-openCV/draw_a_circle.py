import cv2 

path = r'download.jpg'
image = cv2.imread(path)

thick = -3
center_coordinates = (120,50)
radius = 50
colour = (255,255,-780)

circle = cv2.circle(image,center_coordinates,radius,colour,thick)
cv2.imshow('Sample Image',circle)

cv2.waitKey(0)
cv2.destroyAllWindows()