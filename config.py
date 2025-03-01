#!/usr/bin/python3

import os

from dotenv import load_dotenv

load_dotenv()

WATER_SENSOR_LIMIT = os.getenv("WATER_SENSOR_LIMIT")
WATER_DISPENCE_TIME = os.getenv("WATER_DISPENCE_TIME")
WATER_DISPENCE_REST_TIME = os.getenv("WATER_DISPENCE_REST_TIME")
WATER_DISPENCE_TIME_SAFETY_LIMIT = os.getenv("WATER_DISPENCE_TIME_SAFETY_LIMIT")
