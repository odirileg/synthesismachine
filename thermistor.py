import inspect
if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import pyfirmata2 as pyfirmata
import time
import math  # For temperature conversion

# Define Arduino port (Change for Linux/Mac: '/dev/ttyUSBx')
board = pyfirmata.Arduino('/dev/tty.usbserial-1410')
it = pyfirmata.util.Iterator(board)
it.start()

# Define the analog pin where the thermistor is connected
thermistor_pin = board.analog[0]
thermistor_pin.enable_reporting()

# Constants for NTC Thermistor (change based on datasheet)
R_REF = 10000  # Reference resistor value (10kΩ)
BETA = 3950     # Beta coefficient (typical value for NTC thermistors)
T0 = 298.15     # Reference temperature (Kelvin, 25°C = 298.15K)
R0 = 10000      # Resistance at T0 (10kΩ)

# Function to calculate temperature from thermistor voltage
def get_temperature():
    raw_value = thermistor_pin.read()  # Read analog value (0 to 1)
    
    if raw_value is None:
        return None  # Handle cases where data is not available yet

    voltage = raw_value * 5.0  # Convert to voltage
    resistance = (R_REF * voltage) / (5.0 - voltage)  # Voltage divider formula

    # Convert resistance to temperature using Beta equation
    temperature_kelvin = 1 / ((1 / T0) + (math.log(resistance / R0) / BETA))
    temperature_celsius = (temperature_kelvin - 273.15)  # Convert to °C
    
    return round(temperature_celsius, 2)

print(get_temperature())

while True:
    temp = get_temperature()
    
    if temp is not None:
        print(f"Temperature: {temp} °C")
    
    time.sleep(1)  # Read every second

# Read temperature in a loop

# Close connection when done
board.exit()
