import RPi.GPIO as GPIO
from pushbullet import Pushbullet, InvalidKeyError
from datetime import datetime
from os import path
import time

# pip install audioplayer or hover over audioplayer underlined then press on install package if needed!
# for raspberry OS: sudo apt-get install python-gst-1.0 \
#                      gir1.2-gstreamer-1.0 \
#                      gstreamer1.0-tools \
#                      gir1.2-gst-plugins-base-1.0
#                      gstreamer1.0-plugins-good \
#                      gstreamer1.0-plugins-ugly
# Documentation I found: https://pypi.org/project/audioplayer/#API

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Inputs:
sensor = 16

# Outputs:
led_pushbullet = 8
led_alarm = 12
led_safe = 10
buzzer = 24

# Inputs setup:
GPIO.setup(sensor, GPIO.IN)

# Outputs setup:
GPIO.setup(led_pushbullet, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_alarm, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_safe, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(buzzer,GPIO.OUT, initial=GPIO.LOW)

# Additional setup:
doThisOnce = False
pbError = False

# Start program
try:
    api_key = 'o.KQ4eSi8fZz6ym65RT16UyeVRaKq1rslv'
    pb = Pushbullet(api_key)
except InvalidKeyError:
    print("Api Key is invalid")
    pbError = True

# While loop if there is an error connecting to pushbullet api:
while pbError is True:
    GPIO.output(led_pushbullet, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_pushbullet, GPIO.LOW)
    time.sleep(1)

# While loop if there is no error connecting to pushbullet api:
while pbError is False:

    if GPIO.input(sensor):
        if doThisOnce is False:
            GPIO.output(led_alarm, GPIO.HIGH)
            GPIO.output(led_safe, GPIO.LOW)
            GPIO.output(buzzer, GPIO.HIGH)
            pb.push_note("WARNING: FIRE WAS DETECTED!","")
            # add line
            doThisOnce = True

    else:
        if doThisOnce is True:
            GPIO.output(led_alarm, GPIO.LOW)
            GPIO.output(led_safe, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.LOW)
            pb.push_note("FIRE IS UNDER CONTROL!", "")
            # send file
            doThisOnce = False

    # if -------
    #    send file
# 1 add information lkel logs
# 2 find condition => sendlogs()