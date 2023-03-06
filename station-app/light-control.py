#!/usr/bin/env python3

# 52Pi EP-0099 Relay-based RGBW LED light control.
#
# This script manages four relays to control R, G, B, and W light channels on an
# LED light strip. Before running this script, if running on Le Potato's version
# of Raspbian, run the following command to ensure I2C bus is active:
#
#     sudo ldto enable i2c-ao
#
# Otherwise, make sure you can see a device at address 0x10 with `i2cdetect`
#
# The script should flash each of the colors, one after the other, at start.
# Then it will begin monitoring for what color should be currently in use in an
# infinite loop.

import time
import smbus
import sys
import requests

DEVICE_BUS = 0
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)
room_url = 'http://10.0.100.15:5000/room'
room_id = 1
color_map = {'white': 1, 'red': 2, 'green': 3, 'blue': 4}


def startup_light_test():
    print('Beginning light test...')
    for i in range(1,5):
        bus.write_byte_data(DEVICE_ADDR, i, 0xFF)
        time.sleep(1)
        bus.write_byte_data(DEVICE_ADDR, i, 0x00)
    print('...light test complete!')


def lights_out():
    for i in range(1,5):
        bus.write_byte_data(DEVICE_ADDR, i, 0x00)


def set_color(color):
    lights_out()
    relay_id = color_map[color]

    # If the relay is not on, turn it on.
    if True:  # TODO - read smbus data for the address, if it's already on, leave it
        # print('Setting color ' + color)
        bus.write_byte_data(DEVICE_ADDR, relay_id, 0xFF)


def set_lighting():
    try:
        response = requests.get(room_url, {'room_id': room_id})
        response.raise_for_status()
        if response.status_code == 200:
            color = response.json()['color']
            if color == 'off':
                lights_out()
            else:
                set_color(response.json()['color'])
    except:
        print('Received an exception while setting the color. Continuing...')
        # TODO - Should we default to white if there's a problem?


if __name__ == '__main__':
    try:
        startup_light_test()
        print('Monitoring room lighting conditions...')
        while True:
            set_lighting()
            time.sleep(1)
    except KeyboardInterrupt:
        lights_out()
        sys.exit(130)
