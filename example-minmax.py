#! /usr/bin/python3

import time
import sys

EMULATE_HX711=False

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()

    print("Bye!")
    sys.exit()

hx = HX711(20, 21)

hx.set_reading_format("MSB", "MSB")

hx.set_reference_unit(1)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

max_val = -2147483647.0
min_val = 2147483647.0
while True:
    try:
        val = float(hx.get_weight(5))
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
        print("Sensor: {}, MAX: {}, MIN: {}".format(val, max_val, min_val))

        #hx.power_down()
        #hx.power_up()
        time.sleep(0.5)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
