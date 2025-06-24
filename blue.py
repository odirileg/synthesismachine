#from pynput.keyboard import Listener
import pyfirmata
from time import sleep
#import serial.tools.list_ports

print('_________ Bluetooth Controlled LED System ____________')

# Hardcoded Bluetooth port for macOS
portName = "/dev/cu.HC-05"  # Replace with your actual Bluetooth port
print(f'Using hardcoded port: {portName}')

# Connect to Arduino
try:
    print(f'Connecting to {portName}... Please wait.')
    board = pyfirmata.Arduino(portName)
    print('Connected successfully!')
except:
    print('Failed to connect. Check your Bluetooth settings.')
    exit()

# Define LED pins
led_pins = {
    '1': 4,  # LED 1 on D4
    '2': 5,  # LED 2 on D5
}
board.digital[5].write(1)

# Set LED pins as OUTPUT
'''
for pin in led_pins.values():
    board.digital[pin].write(0)  # Ensure all LEDs are off initially

    pin = led_pins["1"]
    current_state = board.digital[pin].read()
    new_state = 1 if current_state == 0 else 0
    board.digital[pin].write(new_state)
    print(f"LED 1: {'ON' if new_state else 'OFF'}")
'''

'''
def toggle_led(led_number):
    if led_number in led_pins:
        pin = led_pins[led_number]
        current_state = board.digital[pin].read() or 0
        new_state = 1 if current_state == 0 else 0
        board.digital[pin].write(new_state)
        print(f"LED {led_number} {'ON' if new_state else 'OFF'}")

# Example usage
while True:
    led_input = input("Enter LED number to toggle (1/2) or 'q' to quit: ")
    if led_input.lower() == 'q':
        break
    toggle_led(led_input)
'''