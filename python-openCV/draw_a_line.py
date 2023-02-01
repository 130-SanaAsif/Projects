import cv2

path = r'image.png.jpg'
image = cv2.imread(path)

start_point = (0,0)
end_point = (100,100)
thickness = 6
colour = (0,0,0)

line = cv2.line(image,start_point,end_point,colour,thickness)
cv2.imshow('Smaple',line)

start_point1 = (100,0)
end_point1 = (0,100)
thick = 6
col = (0,0,0)

line2 = cv2.line(image,start_point1,end_point1,col,thick)
cv2.imshow('Smaple',line2)

cv2.waitKey(0)
cv2.destroyAllWindows()