"""
import hi

hi.hi_world()
"""

#importing packages
import movement
from ultralytics import YOLO
from PIL import Image as img_inst
import os
import matplotlib.pyplot as plt
import glob
import time
import cv2

model = YOLO('path')

def img_resizer(_a):
    newsize=(640,640)
    img = img_inst.open(_a)
    img_resize = img.resize(newsize)
    img_resize_2 = img_resize.rotate(270) #can changed to 'img_resize'
    return img_resize_2

def working():
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

    turning()
    height()
    moving()

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

def starting_inst():
    print('please input what mode you wnat to do')
    print('if you want automode input "automode"')
    print(' if you want self control input "selfmode"')
    text_1 = str(input())

    if text_1 == 'automode':
        working()
    elif text_1 == 'selfmode':
        self_mode()
    else:
        print('please write it again')
        starting_inst()



starting_inst()