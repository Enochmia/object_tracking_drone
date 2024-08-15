import imutils
import requests
import numpy as np
import cv2

url = "http://192.168.35.223:8080//shot.jpg"
  
# While loop to continuously fetching data from the Url
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=640, height=640)
    cv2.imshow("IP Cam", img)
  
    # press q then it'll close
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()