import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        i = 0
        ret, img = cap.read()
        print(img.shape)
        if ret:
            cv2.imshow('camera',img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('Error')
        
else:
    print("Camera Error!")


cv2.destroyWindow('camera')