import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1) # 설정해야됨

throttle = 0
roll = 0
pitch = 0
yaw = 0
option = 0x000f
p_vel = 0x0064
y_vel = 0x0064 # 각각 2바이트

def send_packet():

    startBit_1 = 0x26
    startBit_2 = 0xa8
    startBit_3 = 0x14
    startBit_4 = 0xb1
    length = 0x14 # 각각 1바이트

    payload = bytearray(14)
    
    payload[0] = roll & 0x00ff
    payload[1] = (roll >> 8) & 0x00ff
    payload[2] = pitch & 0x00ff
    payload[3] = (pitch >> 8) & 0x00ff
    payload[4] = yaw & 0x00ff
    payload[5] = (yaw >> 8) & 0x00ff
    payload[6] = throttle & 0x00ff
    payload[7] = (throttle >> 8) & 0x00ff
    payload[8] = option & 0x00ff
    payload[9] = (option >> 8) & 0x00ff
    payload[10] = p_vel & 0x00ff
    payload[11] = (p_vel >> 8) & 0x00ff
    payload[12] = y_vel & 0x00ff
    payload[13] = (y_vel >> 8) & 0x00ff
    
    checkSum = sum(payload) & 0x00ff # 체크섬 1바이트
    
    packet = bytearray([startBit_1, startBit_2, startBit_3, startBit_4, length, checkSum]) + payload # 패킷 수 합계
    
    ser.write(packet)
    print("Sent packet:", packet.hex())

def go_up():
    global throttle
    if throttle < 141:
        throttle += 20
    send_packet()

def go_down():
    global throttle
    if throttle > 9:
        throttle -= 10
    send_packet()

def move_left():
    global roll
    if roll > -200:
        roll -= 40
    send_packet()

def move_right():
    global roll
    if roll < 200:
        roll += 40
    send_packet()

def turn_right():
    global yaw
    if yaw < 170:
        yaw += 10
    send_packet()

def turn_left():
    global yaw
    if yaw > -170:
        yaw -= 10
    send_packet()

def move_forward():
    global pitch
    if pitch < 200:
        pitch += 20
    send_packet()

def move_backward():
    global pitch
    if pitch > -200:
        pitch -= 20
    send_packet()

def landing():
    global throttle
    while throttle > 9:
        throttle -= 10
        send_packet()

def standing():
    global throttle, roll, yaw
    throttle = 100 # 드론이 가만히 떠 있는 숫자를 찾아야 됨
    roll = 0        
    yaw = 0  
    send_packet() 

while True:
    command = input("Enter command").strip()
    
    if command == 'gu':
        go_up()
    elif command == 'gd':
        go_down()
    elif command == 'ml':
        move_left()
    elif command == 'mr':
        move_right()
    elif command == 'tr':
        turn_right()
    elif command == 'tl':
        turn_left()
    elif command == 'mf':
        move_forward()
    elif command == 'mb':
        move_backward()
    elif command == 'landing': 
        landing()
    elif command == 'standing':
        standing()
    else:
        print("다시 입력하세요")
    
    time.sleep(0.1)
