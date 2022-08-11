import cv2

print(cv2.__version__)

img_path = 'cat.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img,[640,480])

print(type(img))
print(img.shape)

if img is not None:
    cv2.imshow(img_path,img)
    cv2.waitKey()
    cv2.destroyAllWindows()

else:
    print("Error!")