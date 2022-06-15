import RPi.GPIO as GPIO

CHANNEL = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

count = 0
while True:
    GPIO.wait_for_edge(CHANNEL, GPIO.FALLING, bouncetime=100)
    count += 1
    print(f"Count = {count}")
