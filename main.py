import RPi.GPIO as GPIO
import audioplayer
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

# Lezemna: Smoke sensor/ detector, 2 green led for ON + SAFE, 1 yellow led for INTERNET/APP/ZINA, 1 red led for ALARM.

# Inputs:
sensor = 8

# Outputs:
led_on = 10
led_internet = 12
led_alarm = 16
led_safe = 18

# Inputs setup:
GPIO.setup(sensor, GPIO.IN)

# Outputs setup:
GPIO.setup(led_on, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led_internet, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_alarm, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(led_safe, GPIO.OUT, initial=GPIO.HIGH)

# Assets setup:
PLAYING = False
ON = audioplayer.AudioPlayer("assets/ON.mp3")
ALARM = audioplayer.AudioPlayer("assets/ALARM.mp3")

# Before while loop, put the code to be executed ONCE, aka when opening the file.
ON.play(block=True)

# While loop:
while True:

    if GPIO.input(sensor):
        GPIO.output(led_alarm, GPIO.HIGH)
        GPIO.output(led_safe, GPIO.LOW)
        if PLAYING is False:
            PLAYING = True
            ALARM.play(loop=True)
    else:
        GPIO.output(led_alarm, GPIO.LOW)
        GPIO.output(led_safe, GPIO.HIGH)
        if PLAYING is True:
            PLAYING = False
            ALARM.stop()