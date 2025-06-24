#from camera import *
from pump_functions import *
from wheel import *
import datetime

#pump assignments
Au_Salt = 5 
PVP_Sln = 6
NaOH = 7

print(f'Time of Synthesis: {datetime.datetime.now()} \n')


def automated_synthesis():
    #dispensing reagent 1
    #dispense(Au_Salt, 20)
    print("20 ml of AuSalt has been dispensed \n")   

    #heat and stir for 2 hours 
    #time.sleep(20)

    #dispense(NaOH, 6)
    print("6 ml of NaOH has been dispensed \n") 

    #camera can watch 
    #stop when the colour matches. while loop can end here
    move_backwards()

    print("The reaction is complete") 



    

automated_synthesis()

