#!/usr/bin/env python3

# Le Potato GPIO Test Script.
#
# This script assumes you have a button's LED attached to pin 40, and the button
# switch attached to pin 38.
#
# When you press the button, the LED should be toggled either on or off.

import gpiod
import sys
import time

# Button 1 Switch: "7J1 Header Pin40"
# Button 1 LED: "7J1 Header Pin38"
# Button 2 Switch: "7J1 Header Pin36"
# Button 2 LED: "7J1 Header Pin35"
# Button 3 Switch: "7J1 Header Pin37"
# Button 3 LED: "7J1 Header Pin33"

bounce_timer = time.perf_counter_ns()
bounce_limit = (5 * 1000000)  # 5ms converted to ns


def rising_edge_detect(event_source, event_value, event_time):
    global bounce_timer

    # A note on debouncing: I tried to find a way using the value to get whether
    # we were truly getting a 'down' click or 'up' release. And I failed.
    # Miserably. There is no reliable way (at least not with the arcade switches
    # I've been testing) to determine whether a press is happening on the down
    # or up side of the falling edge on this board. And we don't have time to
    # print our own debounce circuit, so this function is what you get.
    time_now = time.perf_counter_ns()
    if ((time_now - bounce_timer) > bounce_limit):
        button_click(event_source, event_value, event_time)
        # Reset bounce timer so further noise won't be registered.
        bounce_timer = time.perf_counter_ns()


def button_click(event_source, event_value, event_time):
    print(str(event_source) + ' value: ' + str(event_value) + ' time: ' + str(event_time))


if __name__ == '__main__':
    with gpiod.Chip('periphs-banks') as chip:
        offsets = []

        # Button 1
        button1 = gpiod.find_line("7J1 Header Pin40")
        offsets.append(button1.offset())

        # Button 2
        button2 = gpiod.find_line("7J1 Header Pin36")
        offsets.append(button2.offset())

        # Button 3
        button3 = gpiod.find_line("7J1 Header Pin37")
        offsets.append(button3.offset())

        lines = chip.get_lines(offsets)
        print(lines)
        lines.request(consumer=sys.argv[0], type=gpiod.LINE_REQ_EV_RISING_EDGE, flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP)

        try:
            while True:
                ev_lines = lines.event_wait(sec=1)
                if ev_lines:
                    for line in ev_lines:
                        event = line.event_read()
                        value = line.get_value()
                        rising_edge_detect(event_source = event.source, event_value = value, event_time = str(event.sec) + '.' + str(event.nsec))
        except KeyboardInterrupt:
            sys.exit(130)
