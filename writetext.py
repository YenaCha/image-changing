import cv2
initialimage = cv2.imread('earth.jpg')
font = cv2.FONT_HERSHEY_DUPLEX
startpoint = (50,50)
fontscale = 1
color = (255,0,0)
thickness = 2
newimage = cv2.putText(initialimage, 'cv2', startpoint, font, fontscale, color, thickness)
cv2.imwrite('imagewithtext.jpg', newimage)