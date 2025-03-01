#!/usr/bin/python3
import time

import config
from const import Constants
from gpio import Gpio
from sensor import Sensor

if __name__ == "__main__":
    # initlize
    constants = Constants()
    sensor = Sensor()
    gpio = Gpio(constants.WATER_VALVE_PIN_NUMBER, constants.GPIO_PIN_MODE_OUT)

    # get water sensor value
    voltage = sensor.get_sensor_value_average()
    print("sensor value: %s" % voltage)

    try:
        safety_counter = 0
        # start water dispence
        while (
            voltage < config.WATER_SENSOR_LIMIT
            or safety_counter <= config.WATER_DISPENCE_TIME_SAFETY_LIMIT
        ):
            print("water dispence start")
            gpio.on()
            time.sleep(60 * config.WATER_DISPENCE_TIME)
            print("water dispence rest")
            gpio.off()
            time.sleep(60 * config.WATER_DISPENCE_REST_TIME)
            voltage = sensor.get_sensor_value_average()
            print("sensor value: %s" % voltage)
            safety_counter += 1

        print("finished water dispence")
    except:
        gpio.off()
        gpio.cleanup
