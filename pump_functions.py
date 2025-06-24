from calibration import *

print("PUMPS: CONNECTING \n")
 
initialise_pumps()

print("PUMPS: READY")

#inital values 
initial_volume = 30 
#Reagent_List = ["Aniline", "1-Naphthylaniline", "2,6-Dimethylaniline", "4-Nitroaniline", "Sodium Nitrite", "Sodium Hydroxide", "Solvent"]
#reagent_list_lower = [Reagent_List.lower() for reagent in Reagent_List]

def initialise_volume():
    global Levels
    Levels = [initial_volume] * number_of_pumps
    return Levels

#pump calibrations 
def mils(volume):
    time_required = volume * 0.6
    return time_required

def refill():
    refill_menu = input("Would you like to perform a manual refill (M) or an automatic refill (A)?: ")

    if refill_menu.upper() == 'A':
        auto_reagent_refill = float(input("Please ensure that all reagent vials are filled to the same volume. \n"
                                "Enter the new volume: "))
        global Levels 
        Levels = [auto_reagent_refill] * number_of_pumps
        print(Levels) 
    
    if refill_menu.upper() == 'M':
        individual_reagents_refill = input("\nWhich reagents would you like to refill? "
                           "\nPlease enter in the following format:  "
                           "\nReagent Name, New Volume"
                           "e.g. Aniline, 50 (for a single refill)"
                           "Aniline, 50; Hexane, 10; ...; Reagent Name, Volume in ml (for multiple reagents)"
                           )
       #global Levels
        entries = Levels.split(";")
        for entry in entries:
            try: 
                reagent, refill_volume = entry.split(",")
                reagent = reagent.strip().lower()
                refill_volume = refill_volume.strip()

                if reagent in reagent and refill_volume.isdigit():
                    #Levels[]
                    print("Successful")
            except ValueError:
                pass  

    #come back and complete. finish this indexing thing 

#in progress
'''
def update_volume_tracker():
    #keep track of the volumes as they are aspirated
    new_volume = []
    return Levels 
'''
#haven't started 
def status_check():
    pass 

    #when called, this function should be able to tell us the different levels of the different reagents

def prime_all(): 
    for pump_number in range(pump_pin_start , pump_pin_end + 1): 
        board.digital[pump_number].write(1)
        time.sleep(mils(10))
        board.digital[pump_number].write(0)
        print(pump_number)

def purge_one(pump_number):
    board.digital[pump_number].write(1)
    time.sleep(mils(10))
    board.digital[pump_number].write(0)
    print(f"Pump {pump_number} has been purged")
    
def dispense(pump_number, volume): 
    board.digital[pump_number].write(1)
    print(mils(volume))
    time.sleep(mils(volume))
    board.digital[pump_number].write(0)
    #update_volume_tracker()
