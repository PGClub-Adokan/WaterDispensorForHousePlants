#!/usr/bin/python3

from sensor import Sensor

if __name__ == "__main__":
    sensor = Sensor()
    voltage = sensor.get_sensor_value_average()
    print("average: %s" % voltage)
