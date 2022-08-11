import cv2
import matplotlib.pyplot as plt


img = cv2.imread('cat.jpg')
print(img.shape)
h, w, c = img.shape
cv2.imshow('cat',img)

img2=cv2.resize(img,(int( h*0.5) ,int( w*0.5)))
cv2.imshow('resize',img2)

img3= cv2.flip(img2,flipCode=1) # 1 좌우 0 상하 반전
cv2.imshow('flip', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()