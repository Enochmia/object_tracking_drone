# import movement
from ultralytics import YOLO
from PIL import Image as img_inst
import cv2
import numpy as np

model = YOLO("C:/Users/ludre/Desktop/School_Proj/3rd/14aidrone/0806bf/pt/best_080624.pt")

def img_resizer(_a):
    newsize=(640,640)
    img = img_inst.open(_a)
    img_resize = img.resize(newsize)
    img_resize_2 = img_resize.rotate(270) #can changed to 'img_resize'
    return img_resize_2

def working():
    while True:
        inst_webcam()
        result = model(source=res, conf=0.6)
        try:
            xywhn_inst_1 = result[0].boxes.xywhn.tolist()
            xywhn_inst_xywhn = xywhn_inst_1[0]

            def turning():
                if xywhn_inst_xywhn[0] < 0.4:
                    print('movement.tl()')
                elif xywhn_inst_xywhn[0] > 0.6:
                    print('movement.tr()')
                else:
                    print('movement.standing()')

            def height():
                if xywhn_inst_xywhn[1] < 0.3:
                    print('movement.gd()')
                elif xywhn_inst_xywhn[1] > 0.7:
                    print('movement.gu()')
                else:
                    print('movement.standing()')

            def moving():
                inst_extent_1 = xywhn_inst_xywhn[2]*xywhn_inst_xywhn[3]

                if inst_extent_1 < 0.1:
                    print('movement.mf()')
                elif inst_extent_1 > 0.2:
                    print('movement.mb()')
                else:
                    print('movement.standing()')
            turning()
            height()
            moving()
        except:
            pass

""" #for continuing
    while True:
        result = model(source=img_resizer('path'), conf=0.6, save=True)  
        
        xywhn_inst_1 = result[0].boxes.xywhn.tolist()
        xywhn_inst_xywhn = xywhn_inst_1[0]

        def turning():
            if xywhn_inst_xywhn[0] < 0.4:
                movement.tl()
            elif xywhn_inst_xywhn[0] > 0.6:
                movement.tr()
            else:
                movement.standing()

        def height():
            if xywhn_inst_xywhn[1] < 0.2:
                movement.gd()
            elif xywhn_inst_xywhn[1] > 0.8:
                movement.gu()
            else:
                movement.standing()

        def moving():
            inst_extent_1 = xywhn_inst_xywhn[2]*xywhn_inst_xywhn[3]

            if inst_extent_1 < 0.2:
                movement.mf()
            elif inst_extent_1 > 0.4:
                movement.mb()
            else:
                movement.standing()
"""
"""
def self_mode():
    while True:
        inst_input_1 = str(input())

        if inst_input_1 == 'w':
            movement.mf()
        elif inst_input_1 == 's':
            movement.mb()
        elif inst_input_1 == 'a':
            movement.ml()
        elif inst_input_1 == 'd':
            movement.mr()
        elif inst_input_1 == 'l' or inst_input_1 == 'left':
            movement.tl()
        elif inst_input_1 == 'r' or inst_input_1 == 'right':
            movement.tr()
        elif inst_input_1 == 'q' or inst_input_1 == 'up':
            movement.gd()
        elif inst_input_1 == 'e' or inst_input_1 == 'down':
            movement.gu()
        elif inst_input_1 == 'land':
            movement.landing()
        elif inst_input_1 == 'automode':
            working()
        elif inst_input_1 == 'break':
            movement.standing()
            break
        else:
            movement.standing()
"""
def starting_inst():
    print('please input what mode you wnat to do')
    print('if you want automode input "automode"')
    print('if you want self control input "selfmode"')
    text_1 = str(input())

    if text_1 == 'automode':
        working()
        print('activated')
    elif text_1 == 'selfmode':
        # self_mode()
        print('a')
    elif text_1 == 'test':
        inst_webcam()
    else:
        print('please write it again')
        starting_inst()

        
def inst_webcam():
    url = 'http://192.168.35.223:8080/'
    cap = cv2.VideoCapture(url+'/shot.jpg')
    ret, frame = cap.read()
    global res
    res = cv2.resize(frame, dsize=(640, 640), interpolation=cv2.INTER_CUBIC)
    """
    cv2.imshow("inst", res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # cap.release()
        break
    """
    cap.release()
    # cv2.destroyAllWindows()
        


starting_inst()
