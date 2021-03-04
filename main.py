import RPi.GPIO as GPIO

# pip install playsound fel cmd if necessary.

from playsound import playsound

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Lezemna: smoke sensor/ detector, 1 green led for ON, 1 green led for INTERNET/APP/ZINA, 1 red led for ALARM.

sensor = 8
led_on = 10
led_internet = 12
led_alarm = 16

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led_on, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led_internet, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_alarm, GPIO.OUT, initial=GPIO.LOW)

# Before while loop, put the code to be executed ONCE, aka when opening the file.
playsound('assets/ON.mp3')