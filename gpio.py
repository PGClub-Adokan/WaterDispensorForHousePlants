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
        self._gpio = GPIO
        self._pin_no = pin_number
        self._pin_type = pin_type
        try:
            self._initalize_gpio(gpio_mode)
        except:
            self._gpio.cleanup()
            self._initalize_gpio(gpio_mode)

    def _initalize_gpio(self, gpio_mode):
        self._gpio.setmode(gpio_mode)  # set of numberring type
        self._gpio.setup(self._pin_no, self._pin_type)

    def get(self):
        if self._pin_type == GPIO.IN:
            return self._gpio.input(self._pin_no)
        pass

    def on(self):
        if self._pin_type == GPIO.OUT:
            self._gpio.output(self._pin_no, GPIO.HIGH)
        pass

    def off(self):
        if self._pin_type == GPIO.OUT:
            self._gpio.output(self._pin_no, GPIO.LOW)
        pass

    def cleanup(self):
        try:
            self._gpio.cleanup(self._pin_no)
        except:
            pass

    def __del__(self):
        self.cleanup()
