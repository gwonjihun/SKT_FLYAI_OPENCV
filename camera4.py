import cv2
import matplotlib.pyplot as plt


img = cv2.imread('cat.jpg')
print(img.shape)
cv2.imshow('cat',img)


img2 = img[150:450,150:450].copy()
cv2.line(img2,(0,0),(150,150),(0,0,255),10)
cv2.imshow("crop",img2)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR -> RGB로 전환
cv2.imshow('conver',img)
plt.imshow(img) # matplot은 RGB로 OpenCV는 BGR로 채널입력이 되어있으므로 해당 채널 값을 바꿔줘야한다.
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()