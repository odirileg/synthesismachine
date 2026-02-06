from pump_functions import *
from wheel import *
#from camera import * 
import datetime
from clean_functions import load_reagent_data
print(f'Time of Synthesis: {datetime.datetime.now()} \n')

def automated_synthesis(vials=None, filename="reagent_data.xlsx", generate=True):
    if vials is None:
        vials = int(input("How many vials would you like to use? \n"))

    data = load_reagent_data(vials, filename=filename, generate=generate)
    R1_Name = data["R1_Name"]
    R1 = data["R1"]
    V1 = data["V1"]
    V_Nitrite = data["V_Nitrite"]
    R2_Name = data["R2_Name"]
    R2 = data["R2"]
    V2 = data["V2"]
    V_NaOH = data["V_NaOH"]

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
