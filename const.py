#!/usr/bin/python3


class Constants:
    # For A/D Converter
    @property
    def AD_CONVERTER_PROPS_ANALOG_PIN(self):
        return 0

    @property
    def AD_CONVERTER_PROPS_GAIN(self):
        return 1

    # @see https://tech-and-investment.com/raspberrypi2-5-ads1015/
    #  - 2/3 = +/-6.144V
    #  -   1 = +/-4.096V
    #  -   2 = +/-2.048V
    #  -   4 = +/-1.024V
    #  -   8 = +/-0.512V
    #  -  16 = +/-0.256V
    @property
    def AD_CONVERTER_UNIT_FOR_VOLT_BY_GAIN(self):
        return {
            1: 4.096,
            2: 2.048,
            4: 1.024,
            8: 0.512,
            16: 0.256,
        }

    # Common
    @property
    def WATER_VALVE_PIN_NUMBER(self):
        return 4

    # @property
    # def WATER_SENSOR_LIMIT(self):
    #    return 14600.0

    # @property
    # def WATER_DISPENCE_TIME(self):
    #    return 3  # minute

    # @property
    # def WATER_DISPENCE_REST_TIME(self):
    #    return 7  # minute

    # @property
    # def WATER_DISPENCE_TIME_SAFETY_LIMIT(self):
    #     return 20

    @property
    def GPIO_PIN_MODE_IN(self):
        return 1

    @property
    def GPIO_PIN_MODE_OUT(self):
        return 0
