#!/usr/bin/python3

import RPi.GPIO as GPIO


# if doy you know gpio pin, at see follow link.
# https://www.raspberrypi-spy.co.uk/2012/06/simple-guide-to-the-rpi-gpio-header-and-pins/
class Gpio:
    def __init__(
        self,
        pin_number,
        pin_type=GPIO.IN,
        gpio_mode=GPIO.BCM,
    ):
        self._pin_no = pin_number
        self._pin_type = pin_type
        GPIO.setmode(gpio_mode)  # set of numberring type
        GPIO.setup(self._pin_no, pin_type)

    def get(self):
        if self._pin_type == GPIO.IN:
            return GPIO.input(self._pin_no)
        pass

    def on(self):
        if self._pin_type == GPIO.OUT:
            GPIO.output(self._pin_no, GPIO.HIGH)
        pass

    def off(self):
        if self._pin_type == GPIO.OUT:
            GPIO.output(self._pin_no, GPIO.HIGH)
        pass

    def cleanup(self):
        try:
            GPIO.cleanup(self._pin_no)
        except:
            pass

    def __del__(self):
        self.cleanup
