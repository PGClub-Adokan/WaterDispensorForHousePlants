#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15
import math

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
SENSOR_THRESHOLD = 7500

PIN = 4

values = [0] * 10000

def setup():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIN, GPIO.OUT)
        GPIO.output(PIN, GPIO.HIGH)

def execute():
    maxValue = 0
    ## read some times to avoid pulse value
    for i in range(10000):
        values[i] = adc.read_adc(0, gain = GAIN)
        if values[i] > maxValue:
            maxValue = values[i]
        print("maxValue == " + str(maxValue))
        # if dry
        if (maxValue) <= SENSOR_THRESHOLD:
            GPIO.output(PIN, GPIO.HIGH)
            #GPIO.output(PIN, GPIO.HIGH)
            print("Pump OFF -> ON")
            time.sleep(7)
        #GPIO.output(PIN, GPIO.HIGH)
        #print("Pump ON -> OFF")
        # if not dry
        else:
            #GPIO.output(PIN, GPIO.HIGH)
            GPIO.output(PIN, GPIO.HIGH)
            print("Pump keeps OFF")

def destroy():
    GPIO.output(PIN, GPIO.HIGH)
    GPIO.setup(PIN, GPIO.IN)
    GPIO.cleanup()

if __name__ == '__main__':
        setup()
        try:
                execute()
        except KeyboardInterrupt:
            destroy()
