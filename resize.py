import cv2


img = cv2.imread('cat.jpg')
img = cv2.resize(img,[640,480])

cv2.imwrite('cat.jpg',img)