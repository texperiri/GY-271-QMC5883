## Install I2C
sudo apt-get install git i2c-tools python-smbus python3 python-pip python-virtualenv python3-setuptools

## Activate I2C
sudo raspi-config<br/>
-> Interfacing Options<br/>
-> I2C -> Enable<br/>

## Set baudrate in startup-script
sudo nano /boot/config.txt<br/>
#there search for<br/>
dtparam=i2c_arm=on<br/>
#and extend it to (setting the I2C baudrate to 400kHz)<br/>
dtparam=i2c_arm=on,i2c_arm_baudrate=400000<br/>
#reboot<br/>

## Check if compass module can be detected ("1" is the typical I2C number on a raspberry pi)
sudo i2cdetect -y 1<br/>
example output -> module is found on address 0x0d
```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f<br/>
00:          -- -- -- -- -- -- -- -- -- -- 0d -- --<br/>
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --<br/>
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --<br/>
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --<br/>
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --<br/>
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --<br/>
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --<br/<
70: -- -- -- -- -- -- -- --<br/>
```
## Give i2c rights to non root
sudo nano /etc/udev/rule.d/99-i2c.rules<br/>
#and add the following content<br/>
SUBSYSTEM=="i2c-dev", MODE="0666"

## install python library for I2C access
pip install smbus2

## example python for qmc5883 register configuration and read of x,y,z data (not calibrated)
```
bus = SMBus(1)
addr = 0xd
bus.write_byte_data(addr,0xB,0x1)
bus.write_byte_data(addr,0x9,0x1D)
bus.read_i2c_block_data(addr,0x0,6)
[23, 0, 191, 253, 5, 254]
```
