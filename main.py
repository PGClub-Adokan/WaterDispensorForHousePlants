#!/usr/bin/python3
import time

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
        while voltage < constants.WATER_SENSOR_LIMIT or safety_counter <= 10:
            print("water dispence start")
            gpio.on()
            time.sleep(60 * 3)  # do water dispense 3 minute
            print("water dispence rest")
            gpio.off()
            time.sleep(60 * 7)  # rest water dispence 7 minute
            voltage = sensor.get_sensor_value_average()
            print("sensor value: %s" % voltage)
            safety_counter += 1

        print("finished water dispence")
    except:
        gpio.off()
        gpio.cleanup
