import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        i = 0
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera',img)
            key = cv2.waitKey(1) & 0xFF
            print(key) 
            if key == ord('s'):
                cv2.imwrite(f'mymask{i}.jpg',img)
                i = i+1
        else:
            print('Error')
        
else:
    print("Camera Error!")


cv2.destroyWindow('camera')