from picamera import PiCamera
camera = PiCamera()
import time
from datetime import date

#take picture
def take_picture():
    camera.capture(f"/home/pi/Desktop/{date.today()}R1_V1_R2_V2.jpg")
    
def time_lapse():
    pass

#take video
def record_video():
    video_length = float(input("how long would you like to record?"))
    camera.start_preview()
    camera.start_recording(f'/home/pi/Desktop/{date.today()}R1_V1_R2_V2_video.h264')
    time.sleep(video_length) #stir time 
    camera.stop_recording()
    camera.stop_preview()
     
def video():
    video_length = float(input("how long would you like to record? "))
    video_name = input("what would you like to name this file? ")
    camera.start_preview()
    camera.start_recording(f'/home/pi/Desktop/{video_name}.h264')
    time.sleep(video_length)
    camera.stop_recording()
    camera.stop_preview()
    print("recording complete!")
    
def live_view():
    camera.start_preview()
    time.sleep(10)
    camera.stop_preview()
    print("showing live view")
    
