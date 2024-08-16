import numpy as np
import cv2

# cap = cv2.VideoCapture("path")
"""
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else: 
    break
"""
# cap.release()

# dir_1 = "path"

dir_1 = "path"

# cap = cv2.VideoCapture(dir_1)
# print(f'width:{cap.get(3)} height:{cap.get(4)}')

"""
while True:
    # ret, frame = cap.read()

    cv2.imshow("vid", dir_1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
cv2.destroyAllWindows()
"""

# import imutils
# import requests
"""
url = "path"
  
while True:
    img_req = requests.get(url)
    img_arr = np.array(bytearray(img_req.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=640, height=640)
    cv2.imshow("vid", img)
  
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
"""

url = "path"

while True:
    cv2.imshow("vid", url)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
