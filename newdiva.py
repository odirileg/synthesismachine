import pyfirmata
import time

port = '/dev/tty.usbserial-1420'
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()
time.sleep(1)

motors = {
    'M1': {'DIR': 2, 'STEP': 3, 'EN': 8},
    'M2': {'DIR': 4, 'STEP': 5, 'EN': 9},
    'M3': {'DIR': 6, 'STEP': 7, 'EN': 10},
}

# Setup pins
for m in motors.values():
    board.digital[m['DIR']].mode = pyfirmata.OUTPUT
    board.digital[m['STEP']].mode = pyfirmata.OUTPUT
    board.digital[m['EN']].mode = pyfirmata.OUTPUT
    board.digital[m['EN']].write(1)  # disable initially (HIGH = disabled)

def step_motor(dir_pin, step_pin, en_pin, steps=200, delay=0.005):
    board.digital[en_pin].write(0)  # ENABLE motor (LOW)
    board.digital[dir_pin].write(1)  # Set direction

    for _ in range(steps):
        board.digital[step_pin].write(1)
        time.sleep(delay / 2)
        board.digital[step_pin].write(0)
        time.sleep(delay / 2)

    board.digital[en_pin].write(1)  # DISABLE motor (LOW = enabled)

# Example: run all motors in sequence
step_motor(**motors['M1'])
step_motor(**motors['M2'])
step_motor(**motors['M3'])
