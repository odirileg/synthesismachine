import inspect
if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import pyfirmata2 as pyfirmata 
import time 
from calibration import *

#board information and configuration
initialise_wheel()


def anticlockwise():
    board.digital[13].write(0)
    global direction
    direction = "ANTICLOCKWISE"
    board.digital[2].write(1)
    board.digital[13].write(1)


def clockwise():
    board.digital[13].write(0)
    global direction
    direction = "CLOCKWISE"
    board.digital[2].write(0)
    board.digital[13].write(1)

def state():
    return direction 

def change_direction(): 
    if state() == "CLOCKWISE":
        anticlockwise()  
    elif state() == "ANTICLOCKWISE":
        clockwise()

    return direction

def update_position_tracker():
    #know the position of the wheel at all times
    #when moving in the postive direction, add 1
    #when moving in the neg direction, subtract 1
    global position 
    if state() == "CLOCKWISE":
        position = (position + 1) % places

    elif state() == "ANTICLOCKWISE":
        position = (position - 1) % places
    
    return position    

def move_steps(degrees, speed):
    board.digital[13].write(0)
    steps_per_revolution = 200  # Typical stepper motor has 200 steps per full turn
    step_delay = 1 / speed  # Calculate delay based on speed (in steps per second)

    steps = int(degrees / 1.8)  # Calculate the number of steps for given degrees

    for step in range(steps):
        # Generate step pulse
        board.digital[3].write(1)
        time.sleep(step_delay / 2)  # High pulse

        board.digital[3].write(0)
        time.sleep(step_delay / 2)  # Low pulse

        #print(f"Step: {step + 1}/{steps}")
    board.digital[13].write(1)

def move_backwards():
    anticlockwise()
    move_steps(360, 50)
    update_position_tracker()
    print(f"\nupdated position {position}")

def move_forward():
    clockwise()
    move_steps(360, 50)
    update_position_tracker()
    print(f"\nupdated position {position}")

def move_one():
    if state() == "ANTICLOCKWISE":
        move_backwards()

    elif state() == "CLOCKWISE":
        move_forward()

#this move function works but is a little iffy 
def move_to(destination):
 
    distance = abs(destination - position)
    #move forward
    if destination > position and distance < 12: 
        while distance != 0:
            print(position)
            
            move_forward()
            distance -= 1
    #use modulo to decide 
    if destination > position and distance > 12: 
        moves = 12 - distance%12
        for i in range(1, moves + 1):
            move_backwards()
    
    #move back 
    if destination < position and distance < 12:
        while distance != 0:
            print(f"moving from {position}")
            move_backwards()
            distance -= 1

    #use modulo to decide 
    if destination < position and distance > 12:
        moves = 12 - distance%12 
        for i in range(1, moves + 1):
            move_forward()

    else:
        pass #move forward 

    return position 
    # this should calculate the number of revolutions required to move from one position to the other. use this for calibration

def home():
    global position
    print(f"current: {position}")
    if int(position) > 12:
        print("this is the position > 12 route")
        while position < 24:
            move_one()
            time.sleep(1)
        position = 1

    elif position < 12:
        change_direction()
        print("this is the other route")
        while (position - start) != 0:
            move_one()
            time.sleep(1)
        position = 1

def stir(speed, time):
    pass
