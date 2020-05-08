import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)
while True:
	# read moisture level through capacitive touch pad
	touch = ss.moisture_read()
	# read temperature from the temperature sensor
	temp = ss.get_temp()
	print(time.strftime("%Y-%m-%d %H:%M:%S") + "," + str(temp) + "," + str(touch), flush=True)
	time.sleep(1)
