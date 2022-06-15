import RPi.GPIO as GPIO
import time

CHANNEL = 26
MAX_VALUE = 128

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(CHANNEL, GPIO.FALLING)

count = 0
while True:
    count = (count + 1) % MAX_VALUE
    if GPIO.event_detected(CHANNEL):
        print(count)