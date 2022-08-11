import cv2

print(cv2.__version__)

img_path = 'cat.jpg'
img = cv2.imread(img_path)

print(type(img))
print(img.shape)

if img is not None:
    cv2.imshow('title',img)