import RPi.GPIO as GPIO
import time

CHANNEL = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
while True:
    GPIO.wait_for_edge(CHANNEL, GPIO.FALLING)
    t = time.time() * 1000
    if t % 2 == 0:
        print(1, end="")
    else:
        print(0, end="")