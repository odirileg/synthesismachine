import inspect
if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import pyfirmata2 as pyfirmata
import time

from calibration import *

# Start an iterator to avoid buffer overflow
it = pyfirmata.util.Iterator(board)
it.start()

# Set the A0 pin as an input pin
board.analog[0].mode = pyfirmata.INPUT  # 'a:0:i' for analog pin A0 in input mode
board.analog[0].enable_reporting()


# Allow the board to settle
time.sleep(4)
print(board.analog[0].read())
# Read and print the voltage from A0 in a loop
while True:
    voltage = board.analog[0].read()  # Read the value from the analog pin (0.0 to 1.0)
    if voltage is not None:
        print(f"Voltage from A0: {voltage * 5.0} V")  # Convert to voltage (assuming 5V reference)
    time.sleep(1)
