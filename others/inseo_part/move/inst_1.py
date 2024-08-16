import cv2
# import numpy as np
import imutils
import time
import numpy as np

def inst_webcam():
    url = "http://192.168.35.223:8080/shot.jpg"

    # img_1 = cv2.imread(url)
    # img_arr = np.array(bytearray(img_1), dtype=np.uint8)
    # img_inst = cv2.imdecode(img_arr, -1)
    # img_2 = imutils.resize(img_1, width=640, height=640)
    # cv2.imshow(img_2)
    # time.sleep(10)
    # while True:
    #     cv2.imshow("vid", url)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    
    while True:
        cap = cv2.VideoCapture(url)
        ret, frame = cap.read()
        res = cv2.resize(frame, dsize=(640, 640), interpolation=cv2.INTER_CUBIC)
        cv2.imshow("inst", res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    
    

inst_webcam()
cv2.destroyAllWindows()
"""
import requests
import imutils

url = "http://192.168.35.223:8080/shot.jpg"
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=640, height=640)
    cv2.imshow("Android Cam", img)
  
    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
"""
