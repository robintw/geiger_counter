import RPi.GPIO as GPIO
import time
import sys

CHANNEL = 26
MAX_VALUE = 16

output_filename = sys.argv[1]

try:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(CHANNEL, GPIO.FALLING, bouncetime=100)

    count = 0
    value1 = None
    value2 = None
    bytes_list = []
    while True:
        count = (count + 1) % MAX_VALUE
        if GPIO.event_detected(CHANNEL):
            if value1 is None:
                value1 = count
            else:
                value2 = count

            if value1 is not None and value2 is not None:
                byte_value = (value1 << 4) | value2
                print(byte_value)
                bytes_list.append(byte_value)
except KeyboardInterrupt:
    print(f"Writing output to {output_filename}")
    with open(output_filename, 'wb') as f:
        f.write(bytes(bytes_list))
            
