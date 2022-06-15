import RPi.GPIO as GPIO
import time
import sys

CHANNEL = 26
timer_mins = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(CHANNEL, GPIO.FALLING, bouncetime=100)

count = 0
start_time = time.time()

print("Running...")
while True:
    if time.time() >= start_time + (timer_mins * 60):
        break
    if GPIO.event_detected(CHANNEL):
        count += 1

print(f"Total count over {timer_mins} minutes was {count}")
