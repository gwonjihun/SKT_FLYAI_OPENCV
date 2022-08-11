import cv2
import tensorflow as tf
import numpy as np
import os
import tensorflow as tf

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")
model = tf.keras.models.load_model('C:\\Users\\027\\Desktop\\opencv\\weights\\my_mask_model.h5')

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        i = 0
        ret, img = cap.read()
        print(img.shape)

        if ret:
            x_data = cv2.resize(img,(480,480)).copy()
            x_data = cv2.cvtColor(x_data,cv2.COLOR_BGR2RGB)
            print(x_data.shape)
            x_data = np.array(x_data)
            x_data = x_data.reshape(-1,480,480,3)
            x_data = x_data/255.0
            print("1")
            x_pred = model.predict(x_data)
            print("2")
            
            if np.around(x_pred)== 0:
                cv2.putText(img,'Mask',(20,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0))
            else:
                cv2.putText(img,'NOMask',(20,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255))

            cv2.imshow('camera',img)
            if cv2.waitKey(1) != -1:
                break
        else:
            print('Error')
        
else:
    print("Camera Error!")


cv2.destroyWindow('camera')