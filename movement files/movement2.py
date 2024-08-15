throttle = 0

roll = 0

yaw = 0

pitch = 0

# 위로 이동
def go_up():
    global throttle
    if throttle < 141:
        throttle += 20
# 아래로 이동
def go_down():
    global throttle
    if throttle > 9:
        throttle -= 10
# 왼쪽으로 이동
def move_left():
    global roll
    if roll > -200:
        roll -= 40
# 오른쪽으로 이동
def move_right():
    global roll
    if roll < 200:
        roll += 40
# 오른쪽 회전
def turn_right():
    global yaw
    if yaw < 170:
        yaw += 10
# 왼쪽 회전
def turn_left():
    global yaw
    if yaw > -170:
        yaw -= 10
# 앞으로 전진
def move_forward():
    global pitch
    if pitch < 200:
        pitch += 20
# 뒤로 후진
def move_backward():
    global pitch
    if pitch > -200:
        pitch -= 20
# 착륙 
def landing():
    global throttle
    while throttle > 9:
        throttle -= 10
# 공중에 떠있기
def standing():
    global throttle, roll, yaw, pitch
    throttle = 100
    roll = 0        
    yaw = 0 
    pitch = 0
  
while True:
    command = input("Enter command")
    
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
    elif command =='standing':
        standing()
    else:
        print("잘못된 명령어 입니다")