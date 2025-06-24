from pump_functions import *
from wheel import *
#from camera import * 
import datetime
from clean_functions import *
print(f'Time of Synthesis: {datetime.datetime.now()} \n')

def automated_synthesis():
    #dispensing reagent 1
    for i in range(0, vials):
        print(f'{V1[i]} ml of {R1_Name[i]} is being dispensed into vial {i+1}')
        dispense((R1[i]), V1[(i)])
        time.sleep(3)
        move_forward()
   
    print("The first primary amine has been successfully dispensed. Now dispensing the nitrite salt. \n")   
    
    home()  

    print("Moving to position 1")

    #stir()

    #dispensing Nitrite
    for j in range(0, vials):
        print(f'{V_Nitrite[j]} ml of NaNO2 is being dispensed into vial {j+1}')
        dispense((R1[j]), V_Nitrite[(j)])
        time.sleep(3)
        move_steps(360, 20)

    print("\nThe nitrite salt has been successfully dispensed. Now dispensing the second primary amine. \n")
   
    #dispensing reagent 2
    for k in range(0, vials):
        print(f'{V2[k]} ml of {R2_Name[k]} is being dispensed into vial {k+1}')
        dispense((R2[k]), V2[(k)])
        time.sleep(3)
        move_steps(360, 20)
        
    print("\nThe second primary amine has been successfully dispensed. Now dispensing the hydroxide salt. \n")

    #dispensing Hydroxide 
    for m in range(0, vials):
        print(f'{V_NaOH[m]} ml of NaOH is being dispensed into vial {m+1}')
        dispense((R1[m]), V_NaOH[(m)])
        time.sleep(3)
        move_steps(360, 20)
        

    print(f"Reaction complete at {datetime.datetime.now()}")   


automated_synthesis()

