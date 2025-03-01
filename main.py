#!/usr/bin/python3
import time

from const import Constants
from gpio import Gpio
from sensor import Sensor

if __name__ == "__main__":
    # initlize
    constants = Constants()
    sensor = Sensor()
    gpio = Gpio(constants.WATER_VALVE_PIN_NUMBER)

    # get water sensor value
    voltage = sensor.get_sensor_value_average()

    try:
        safety_counter = 0
        # start water dispence
        while voltage < constants.WATER_SENSOR_LIMIT or safety_counter <= 10:
            gpio.on()
            time.sleep(60 * 1)  # do water dispense 1 minute
            gpio.off()
            time.sleep(60 * 4)  # rest water dispence 4 minute
            safety_counter += 1
    except:
        gpio.cleanup
