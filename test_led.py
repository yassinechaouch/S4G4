import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

sensor = 10
led = 8
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(sensor, GPIO.IN)


while True:
    if GPIO.input(sensor):
        GPIO.output(led,GPIO.HIGH)
    else:
        GPIO.output(led,GPIO.LOW)

