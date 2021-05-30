# micropython-ad840x

Micropython SPI-based manipulation of the AD series digital potentiometers AD8400, AD8402 and AD8403.

This has been tested with ESP8266 and ESP32 running Micropython 1.15 on AD8402 only, but should work also with AD8400 and AD8403. Please post an issue if you have success.

## Pins
You can connect the AD840x to the following Pins:

Pin (AD840x)  | Pin (ESP32)      | Description
:------------:|:----------------:|:----------------------------------------
CS    	      | HSPID (GPIO13)   | Chip Select Input
CLK           | HSPICLK (GPIO14) | Serial Clock Input
SDI           | HSPICS0 (GPIO15) | Serial Data Input


```python
from machine import SPI
import ad840x

#Setting up the SPI system
spi = SPI(1)

#Initalize the AD840x
poti_1channel = ad840x.AD8400(spi, cs=15)
poti_2channel = ad840x.AD8402(spi, cs=16)
poti_4channel = ad840x.AD8403(spi, cs=17)

#Set Channel 0
poti_1channel.write(0, 0) #Zero-scale (wiper contact resistance)
poti_2channel.write(0, 50) #Midscale
poti_4channel.write(0, 100) #Full scale

#Set Channel 1 in raw mode
poti_2channel.write_raw(1, 0) #Zero-scale (wiper contact resistance)
poti_4channel.write_raw(1, 128) #Midscale

#Set Channel 2
poti_4channel.write(2, 100) #Full scale

#Set Channel 3 in raw mode
poti_4channel.write(3, 255) #Full scale
```
