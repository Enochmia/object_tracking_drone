import cv2
import numpy as np

url = 'path'

while True:
    cap = cv2.VideoCapture(url+'/shot.jpg')
    ret, frame = cap.read()
    res = cv2.resize(frame, dsize=(640, 640), interpolation=cv2.INTER_CUBIC)
    cv2.imshow("inst", res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cap.release()
        break
cap.release()
cv2.destroyAllWindows()