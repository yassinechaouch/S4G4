import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

sensor = 10
led = LED(8)
GPIO.setup(sensor, GPIO.IN)


while True:
    if GPIO.input(sensor):
        led.on()
    else:
        led.off()

