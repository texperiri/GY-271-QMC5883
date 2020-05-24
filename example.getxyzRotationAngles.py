#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
from qmc5883 import QMC5883

#initialize with the offsets read with example.getCalibration.py
#example output:
#xMin[-5510],xMax[5740],xOffset[-115],yMin[-8215],yMax[2977],yOffset[2619],zMin[-5610],zMax[5025],zOffset[292]
compass = QMC5883(xOffset = -115 , yOffset = 2619 , zOffset = 292)

while True:
	(dataReady,dataOverflow,dataSkippedForReading) = compass.status()
	if (dataReady == 1):
		(x,y,z,rotX,rotY,rotZ) = compass.heading()
		sys.stdout.write("\rHeading: rotX={:3.0f}° rotY={:3.0f}° rotZ={:3.0f}° [x={:5.0f},y={:5.0f},z={:5.0f}], overflow={}, skip={}, Temp={}°C".format(rotX,rotY,rotZ,x,y,z,dataOverflow,dataSkippedForReading,compass.getTemperature()))
		sys.stdout.flush()
	time.sleep(0.5)
