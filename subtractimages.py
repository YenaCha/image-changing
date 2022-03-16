import cv2
image3 = cv2.imread('image3.jpg')
image4 = cv2.imread('image4.jpg')
subtractedimage = cv2.subtract(image3,image4)
cv2.imwrite('finalimage2.jpg', subtractedimage)