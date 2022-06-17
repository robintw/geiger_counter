import RPi.GPIO as GPIO
import time

CHANNEL = 26

def get_time_of_event():
    GPIO.wait_for_edge(CHANNEL, GPIO.FALLING, bouncetime=100)
    return time.time()

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
t1 = None
t2 = None
t3 = None
while True:
    new_event_time = get_time_of_event()
    t1 = t2
    t2 = t3
    t3 = new_event_time

    if not any([t1 is None, t2 is None, t3 is None]):
        diff1 = t2 - t1
        diff2 = t3 - t2
        if diff2 > diff1:
            print("1", end="", flush=True)
        else:
            print("0", end="", flush=True)
    else:
        print("Not enough data")
