import cv2
import numpy as np

cap = cv2.VideoCapture(0)

tmp = 0
while cap.isOpened():
    ret, frame = cap.read()
    #print(frame.shape)
    if ret:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('s'):
            file_name = f'mask/mask{tmp}.jpg'
            cv2.imwrite(file_name, frame)
            print(file_name + ' is saved.')
            tmp += 1
        elif cv2.waitKey(1) == ord('q'):
            break
        
    else:
        print('Error!')

cv2.destroyAllWindows()
cap.release()