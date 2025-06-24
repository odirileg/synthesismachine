import pyfirmata
import time

port = input("port number /dev/...: ")

board = pyfirmata.Arduino(f"/dev/{port}")
it = pyfirmata.util.Iterator(board)
it.start()

#pump information 
number_of_pumps = 8
pump_pin_start = 4
pump_pin_end = number_of_pumps + pump_pin_start

thermistor_pin = 1

#wheel information 
start = 1
position = 1
direction = "CLOCKWISE"
places = 24

def initialise_syringes(): 
    pass


def tester(pin): 
    board.digital[pin].mode = pyfirmata.INPUT
    
def initialise_pumps():
    #pump assignments
    for pump_number in range(pump_pin_start, pump_pin_end):
        print(f'{pump_number} is ready')
        board.digital[pump_number].mode = pyfirmata.OUTPUT 

#Pump Assignments 
pump_map = {
    "Aniline": 4,
    "2,6-Dimethylaniline": 5,
    "4-Nitroaniline": 6,
    "Naphthyamine": 7,
    "NaNO3" : 8,
    "NaOH": 9
}

def initialise_thermistor():
    board.analog[thermistor_pin].mode = pyfirmata.INPUT
    board.analog[thermistor_pin].enable_reporting()
    time.sleep(5)

    

def initialise_wheel(direction_pin = 2, step_pin = 3):
    print("WHEEL: CONNECTING")
    board.digital[13].write(1) #quiet wheel
    board.digital[direction_pin].mode = pyfirmata.OUTPUT #direction
    board.digital[step_pin].mode = pyfirmata.OUTPUT #steps
    print("WHEEL: READY")

def initialise_fans():
    print("FAN: CONNECTING")
    board.get_pin('d:12:o')
    print("FAN: READY")
