import RPi.GPIO as GPIO
import time
import sys

CHANNEL = 26
MAX_VALUE = 16

output_filename = sys.argv[1]

file_id = 1

def write_file(bytes_list):
    output_filename = output_filename + "_" + str(file_id)
    file_id += 1
    print(f"Writing output to {output_filename}")
    with open(output_filename, 'wb') as f:
        f.write(bytes(bytes_list))

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
                print(bin(value1))
                print(bin(value2))
                byte_value = (value1 << 4) | value2
                print(byte_value)
                bytes_list.append(byte_value)
                value1 = None
                value2 = None

                if len(bytes_list) >= 1024:
                    write_file(bytes_list)
                    bytes_list = []
except KeyboardInterrupt:
    write_file(bytes_list)
            