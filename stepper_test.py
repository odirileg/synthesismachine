from calibration import *
from button import *
import datetime as dt
'''
port = '/dev/tty.usbserial-1420'
board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start()
'''

silencer = 8
board.digital[2].mode = pyfirmata.OUTPUT #direction
board.digital[3].mode = pyfirmata.OUTPUT #steps

board.digital[4].mode = pyfirmata.OUTPUT #direction
board.digital[5].mode = pyfirmata.OUTPUT #steps
board.digital[6].mode = pyfirmata.OUTPUT #direction
board.digital[7].mode = pyfirmata.OUTPUT #steps
board.digital[silencer].mode = pyfirmata.OUTPUT #steps

board.digital[silencer].write(1)
board.digital[2].write(0)

velocity = 100

def forwards(syringe):
    global direction 
    direction = "FORWARDS"
    board.digital[syringe-1].write(1)
    return direction

def backwards(syringe):
    global direction 
    direction = "BACKWARDS"
    board.digital[syringe-1].write(0)
    return direction

def state():
    return direction 

def change_direction(syringe): 
    if state() == "BACKWARDS":
        forwards(syringe)  
    elif state() == "FORWARDS":
        backwards(syringe)
    return direction

def centimeters(travel):
    mm = travel*(360/8)
    return mm
    
def vol_ml(vol):
    ml = 6 * centimeters(vol)
    return ml

#button 


def cali_syringe():
    pass

def move_steps(number,degrees, speed):
    board.digital[silencer].write(0)
    step_delay = 1 / speed  
    steps = int(degrees / 1.8)  
    global velocity 
    velocity = speed 

    for step in range(steps):
        board.digital[number].write(1)
        time.sleep(step_delay / 2) 
        board.digital[number].write(0)
        time.sleep(step_delay / 2)  
    board.digital[silencer].write(1)

def move_forwards(syringe):
    forwards(syringe)
    move_steps(syringe, 720, 100)

def move_backwards(syringe):
    backwards(syringe)
    move_steps(syringe, 720, 100)   

def move_distance(syringe, distance): 
    distance = centimeters(distance)
    move_steps(syringe, distance, 200)

def get_speed(): 
    global velocity
    return velocity

def measure_distance(syringe, distance):
    global velocity
    distance = distance
    start = dt.datetime.now()
    move_distance(syringe, distance)
    end = dt.datetime.now()
    dtime = end - start
    get_speed()
    #calc_distance = dtime*velocity
    return dtime #change time to seconds and use those to convert to mm

def dispense(syringe, volume):
    dis = vol_ml(volume)
    print(dis)
    move_steps(syringe, dis, 50)
    
def home_syringe(syringe):
    while not clicked():
        move_forwards(syringe)
        time.sleep(0.01)
    print("clicked")
    change_direction(syringe)
    move_distance(syringe, 50)
  
#forwards(3)
#move_distance(3, 20)
#home_syringe(5)
#dispense(5, 2)
move_steps(5, 360, 200)

print(measure_distance(3, 8))
'''
time.sleep(5)
move_steps(3, 540, 100)
'''



