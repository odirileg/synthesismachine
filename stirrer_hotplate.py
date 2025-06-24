from  calibration import * 
import time 


initialise_fans()

def stir(stir_time, stir_speed):
    board.digital[12].write(1)
    time.sleep(float(stir_time))
    board.digital[12].write(0)
    
def pulse_fan():
    stir(1, 50)
    time.sleep(1)
    

pulse_fan()