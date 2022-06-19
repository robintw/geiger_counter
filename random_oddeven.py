import RPi.GPIO as GPIO
import time
import sys

CHANNEL = 26
output_filename = sys.argv[1]


try:
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(CHANNEL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    count = 0
    binary_string = ""
    bytes_list = []
    while True:
        GPIO.wait_for_edge(CHANNEL, GPIO.FALLING, bouncetime=200)
        t = time.time() * 1000
        binary_value = int(int(t) % 2 == 0)
        if binary_value:
            print(1, end="", flush=True)
            binary_string += "1"
        else:
            print(0, end="", flush=True)
            binary_string += "0"

        if len(binary_string) == 8:
            byte_value = int(binary_string, base=2)
            bytes_list.append(byte_value)
            print("\n")
            print(f"Byte value = {byte_value}")
            print(f"Current output length = {len(bytes_list)}")
except KeyboardInterrupt:
    print(f"Writing output to {output_filename}")
    with open(output_filename, 'wb') as f:
        f.write(bytes(bytes_list))