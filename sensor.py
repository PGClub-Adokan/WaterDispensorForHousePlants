#!/usr/bin/python3

import Adafruit_ADS1x15  # A/D Conveter Driver
import numpy

from const import Constants


# センサーの制御
class Sensor:
    def __init__(self):
        self._sensor_driver = Adafruit_ADS1x15.ADS1115()
        self.constants = Constants()
        self._unit_for_voltage = self._calc_unit_for_voltage(
            self.constants.AD_CONVERTER_PROPS_GAIN
        )

    def _calc_unit_for_voltage(self, gain):
        return self.constants.AD_CONVERTER_UNIT_FOR_VOLT_BY_GAIN[gain] * 2 / 4.096

    def get_sensor_value_average(self):
        sensor_values = [0] * 100

        for i in range(100):
            sensor_value = self._sensor_driver.read_adc(
                self.constants.AD_CONVERTER_PROPS_ANALOG_PIN,
                gain=self.constants.AD_CONVERTER_PROPS_GAIN,
            )
            sensor_value = self._sensor_driver.read_adc(0, 1)
            sensor_values[i] = float(sensor_value) * float(self._unit_for_voltage)
            print("current voltage: %s" % sensor_values[i])

        return numpy.average(sensor_values)
