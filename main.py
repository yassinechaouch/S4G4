import RPi.GPIO as GPIO
from pushbullet import Pushbullet, InvalidKeyError
from datetime import datetime
import log_manager
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Inputs:
sensor = 13

# Outputs:
led_pushbullet = 8
led_alarm = 12
led_safe = 10
buzzer = 24

# Inputs setup:
GPIO.setup(sensor, GPIO.IN)

# Outputs setup:
GPIO.setup(led_pushbullet, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led_alarm, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_safe, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buzzer,GPIO.OUT, initial=GPIO.LOW)

# Additional setup:
doThisOnce = False
pbError = False
begin = 0
end = 0
duration = 0
current_date_and_time = 0
counter = 0
# Start program

print("Initialize")
time.sleep(15)
print("Done")

try:
    api_key = 'o.VD9eRgkRKHauErawHzO8KN4qAWqXCysG'
    pb = Pushbullet(api_key)
except InvalidKeyError:
    print("Api Key is invalid")
    pbError = True

if pbError is False:
    GPIO.output(led_pushbullet,GPIO.LOW)
    GPIO.output(led_safe,GPIO.HIGH)

# While loop if there is an error connecting to pushbullet api:
while pbError is True:
    GPIO.output(led_pushbullet, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pushbullet, GPIO.LOW)
    time.sleep(1)

# While loop if there is no error connecting to pushbullet api:
while pbError is False:
    time.sleep(0.2)
    if not GPIO.input(sensor):
        if doThisOnce is False:
            print("In")
            GPIO.output(led_alarm, GPIO.HIGH)
            GPIO.output(led_safe, GPIO.LOW)
            GPIO.output(buzzer, GPIO.HIGH)
            begin = time.time()
            now = datetime.now()
            current_date_and_time = now.strftime("%d/%m/%Y %H:%M:%S")
            pb.push_note("WARNING: FIRE WAS DETECTED!","")
            doThisOnce = True

    else:
        print("Stand By")
        GPIO.output(led_safe, GPIO.HIGH)
        if doThisOnce is True:
            print("Out")
            GPIO.output(led_alarm, GPIO.LOW)
            GPIO.output(buzzer, GPIO.LOW)
            end = time.time()
            duration = end - begin
            pb.push_note("FIRE IS UNDER CONTROL!", "")
            log_manager.add_line_to_file(current_date_and_time,duration)
            log_manager.send_file(pb)
            doThisOnce = False