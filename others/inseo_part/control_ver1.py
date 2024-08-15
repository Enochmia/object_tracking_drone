# import movement
from ultralytics import YOLO
from PIL import Image as img_inst
import cv2
import numpy as np

model = YOLO("path") # your yolo model weight file path

def img_resizer(_a): # for more wider use
    newsize=(640,640)
    img = img_inst.open(_a)
    img_resize = img.resize(newsize)
    img_resize_2 = img_resize.rotate(270) #can changed to 'img_resize'
    return img_resize_2

def working():
    while True:
        inst_webcam()
        result = model(source=res, conf=0.6)
        try: # if there nothing that had been detected causes error so added this
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
                inst_extent_1 = xywhn_inst_xywhn[2]*xywhn_inst_xywhn[3] # I would rather use area than W or H

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

def self_mode(): # pygame or else would be great but :/
    while True:
        inst_input_1 = str(input())

        if inst_input_1 == 'w':
            print('movement.mf()')
        elif inst_input_1 == 's':
            print('movement.mb()')
        elif inst_input_1 == 'a':
            print('movement.ml()')
        elif inst_input_1 == 'd':
            print('movement.mr()')
        elif inst_input_1 == 'l' or inst_input_1 == 'left':
            print('movement.tl()')
        elif inst_input_1 == 'r' or inst_input_1 == 'right':
            print('movement.tr()')
        elif inst_input_1 == 'q' or inst_input_1 == 'up':
            print('movement.gd()')
        elif inst_input_1 == 'e' or inst_input_1 == 'down':
            print('movement.gu()')
        elif inst_input_1 == 'land':
            print('movement.landing()')
        elif inst_input_1 == 'automode':
            working()
        elif inst_input_1 == 'break':
            print('movement.standing()')
            break
        else:
            print('movement.standing()')

def starting_inst(): # mode typing
    print('please type what mode you wnat to do')
    print('if you want automode type "automode"')
    print('if you want self control type "selfmode"')
    print('if you are testing something type "test"')
    text_1 = str(input())

    if text_1 == 'automode':
        working()
        print('activated')
    elif text_1 == 'selfmode':
        self_mode()
        print('activated')
    elif text_1 == 'test':
        inst_webcam()
        print('activated')
    else:
        print('please write it again')
        starting_inst()

def inst_webcam(): # test and else
    url = 'path' #I used IP webcam application made by "Thyoni Tech"
    cap = cv2.VideoCapture(url+'/shot.jpg')
    ret, frame = cap.read()
    global res # global variable "res" so i can use it at other def
    res = cv2.resize(frame, dsize=(640, 640), interpolation=cv2.INTER_CUBIC) #resizing is for better performance cuz my computer is not that good :/
    
    """ # these codes were for testing
    cv2.imshow("inst", res)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        # cap.release()
        # cv2.destroyAllWindows() 
        break
    """

    cap.release() # Don't know it should be released but for better performance i released(?)



starting_inst() # starting the program