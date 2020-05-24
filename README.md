# GY-271-QMC5883
Python sample code for using the GY-271 compass module based on the QMC5883 Chip

## Python-Package Requirements
* smbus2 [pip install smbus2]

## Usage-Examples see
* example.getxyzRotationAngles.py
* example.getCalibration.py


## What you need to get usable readings
The QMC5883 chips i got were quite well calibrated for the x and the z axis, but not for the y-axis.
Therfore holding the chip hoizontal and rotating it about the z-axis gave nonsense-readings.

The calibration I do in the driver is very simple - one offset value for every axis.
The offset is calculated using the min and max values you get from every axis.

The script "example.getCalibration.py" helps you get the min/max values and the calculated offsets.
Simply start the script and turn your sensor about every axis for at least 360 degrees ... and then do some random turnings.
Do this until the output of the script doesn't change any more.
Note the xOffset, yOffset and zOffset values and use them as initialization values for the qmc5883 driver
- see example.getxyzRotationAngles.py

## Output of qmc5883.heading()
* x,y,z ... the (offset-corrected) x,y,z readings
* rotX,rotY,rotZ ... the rotation angle about the x,y and z-Axis

Typically (when you hold the chip horizontally and z axis pointing up) rotZ gives you the angle between the x-axis and magnetic "north"
* rotX: when x points up - angle between y-axis and magnetic "north"
* rotY: when y points up - angle between z-axis and magnetic "north"


## Not yet done
... add the magnetic declination into the calculation of rotX,Y,Z
http://magnetic-declination.com










