#!/usr/bin/env python
# -*- coding: utf-8 -*-

from qmc5883 import QMC5883

#initialize with offsets = 0
compass = QMC5883(xOffset = 0, yOffset = 0, zOffset = 0)

#turn your sensor during calibration in all directions until there are no more changes
#Abort the calibrate-script with CTRL+C
#note the xOffset,yOffset and zOffset values and use them for the initialzation of the sensor.
compass.calibrate()
