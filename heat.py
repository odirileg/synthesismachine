from calibration import *
import math

initialise_thermistor()

volt_in = board.analog[thermistor_pin].read()
#read_value = board.get_pin('a:1:i').read()
print(volt_in)

#read_value = board.analog[1].read()  # Trying pin A1 instead
print("Analog A1 value:", volt_in*1024)

'''
if read_value is None:
    print("Failed to read from sensor")
    read_value = 0  # Set to a default value or handle appropriately
else:
    read_value = float(read_value)

def get_temperature(read_value):
    if read_value == 0:
        return -273.15
    
    else:
        temp_log = float(math.log(10240000/read_value-10000))
        temp_K = float(1/(0.001129148 + (0.000234125 * temp_log) + (0.0000000876741 * (temp_log **3))))
        temp_C = float(temp_K - 273.15)
        return temp_C
                    
while True:
    temperature = (get_temperature(read_value))
    print(f"Temp: {temperature} ºC") 
    time.sleep(2)   
'''