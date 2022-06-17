import RPi.GPIO as GPIO
import time

CHANNEL = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.wait_for_edge(CHANNEL, GPIO.FALLING, bouncetime=100)
    print(time.time())
