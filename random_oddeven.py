import RPi.GPIO as GPIO
import time

CHANNEL = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
while True:
    GPIO.wait_for_edge(CHANNEL, GPIO.FALLING, bouncetime=200)
    t = time.time() * 1000
#    print(t)
    if int(t) % 2 == 0:
        print(1, end="", flush=True)
    else:
        print(0, end="", flush=True)
