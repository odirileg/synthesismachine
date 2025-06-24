from calibration import * 
import datetime 
from pump_functions import *

vol = (100/.895)

initialise_pumps()
print(f"starting: {datetime.datetime.now()}")
dispense(5, (vol))
print(f"done: {datetime.datetime.now()}")
