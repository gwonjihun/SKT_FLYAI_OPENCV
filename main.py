import cv2

print(cv2.__version__)

img_path = 'cat.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img,[640,480])
img2 = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2,[640,480])
print(type(img))
print(img.shape)

if img is not None:
    cv2.imshow(img_path,img)
    cv2.imshow("gray",img2)
    cv2.waitKey()
    # 이미지 파일 저장
    cv2.imwrite('cat_gray.jpg',img2)
    cv2.destroyAllWindows()

else:
    print("Error!")