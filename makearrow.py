import cv2
initialimage = cv2.imread('earth.jpg')
startpoint = (255,0)
endpoint = (0,90)
color = (0,0,255)
thickness = 9
arrowdedimage = cv2.arrowedLine(initialimage, startpoint, endpoint, color, thickness)
cv2.imwrite('imagewitharrow.jpg', arrowdedimage)