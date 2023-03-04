#!/usr/bin/env python3

# 52Pi EP-0099 Relay test script.
#
# This script turns on each of the four relays for 1s with a 1s delay between
# relays. Before running this script, if running on Le Potato's version of
# Raspbian, run the following command to ensure I2C bus is active:
#
#     sudo ldto enable i2c-ao
#
# Otherwise, make sure you can see a device at address 0x10 with `i2cdetect`

import time as t
import smbus
import sys

DEVICE_BUS = 0
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)

while True:
    try:
        for i in range(1,5):
            bus.write_byte_data(DEVICE_ADDR, i, 0xFF)
            t.sleep(1)
            bus.write_byte_data(DEVICE_ADDR, i, 0x00)
            t.sleep(1)
    except KeyboardInterrupt as e:
        print("Quit the Loop")
        sys.exit()
