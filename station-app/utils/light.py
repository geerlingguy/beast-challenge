#!/usr/bin/env python3
# Script for quick light testing.
#
# Usage:
#   ./light.py red  # turn on red light
#   ./light.py off  # turn off light

import time
import smbus
import sys
import requests

DEVICE_BUS = 0
DEVICE_ADDR = 0x10
bus = smbus.SMBus(DEVICE_BUS)
color_map = {'white': 1, 'red': 2, 'green': 3, 'blue': 4}


def lights_out():
    for i in range(1,5):
        bus.write_byte_data(DEVICE_ADDR, i, 0x00)


def set_color(color):
    lights_out()
    relay_id = color_map[color]
    bus.write_byte_data(DEVICE_ADDR, relay_id, 0xFF)


if __name__ == '__main__':
    try:
        color = sys.argv[1]
        if color == 'off':
            lights_out()
        else:
            set_color(color)
    except KeyboardInterrupt:
        lights_out()
        sys.exit(130)