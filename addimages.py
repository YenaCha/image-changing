import cv2
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')
addedimage = cv2.addWeighted(image1, 0.7, image2, 0.3,0)
cv2.imwrite('finalimage.jpg', addedimage)