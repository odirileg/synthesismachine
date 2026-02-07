from calibration import * 
button = 9
board.digital[button].mode = pyfirmata.INPUT 

time.sleep(1)
previous_state = 0 

def clicked():
    global previous_state
    current_state = board.digital[button].read()
    if current_state is None:
        return False 
    
    if not previous_state and current_state == 1:
        previous_state = True 
        return True 
    
    previous_state = current_state
    return False
    


'''

while not clicked():
    print(".")
    time.sleep(1)

print('done')
 
'''