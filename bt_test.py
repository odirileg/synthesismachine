import serial

port = "/dev/cu.HC-05"  # Change to your Bluetooth module's port
baud_rate = 9600  # Match what you set in Firmata

try:
    bt_serial = serial.Serial(port, baud_rate, timeout=1)
    print("Connected to Bluetooth module")
    
    bt_serial.write(b'Hello Arduino\n')  # Send test message
    response = bt_serial.readline().decode().strip()
    print("Response from Arduino:", response)

except Exception as e:

    print("Error:", e)
