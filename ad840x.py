from machine import SPI, Pin

class AD840X():
    """
    Base class to represent an AD840x series digital potentiometer.
    """
    def __init__(self, spi, cs: int):
        self.spi = spi
        self.cs = Pin(cs, Pin.OUT, value=1)
        self.channel = 0
        self.value = 0

    def _validate_channel(self, channel):
        """Raise an exception if channel is outside th range of allowed values."""
        if channel > self.CHANNELS:
            raise ValueError('Invalid channel value, must be between 0 and {0}.'.format(self.CHANNELS))

    def _write(self, channel: int, value: int):
        """Write the given value to the given channel"""
        self.channel = bytearray(1)
        self.value = bytearray(1)
        self.channel[0] = channel
        self.value[0] = value

        self.cs.off()
        self.spi.write(self.channel)
        self.spi.write(self.value)
        self.cs.on()

    def write_raw(self, channel:int, value: int):
        """
        Write an RAW value to the potentiometer.
        0 = Zero-scale (wiper contact resistance)
        1 = 1 LSB
        128 = Midscale
        >=255 = Full scale
        """
        self._validate_channel(channel)
        self._write(channel, value)

    def write(self, channel:int, value: int):
        """
        Write an percentage value to the potentiometer.
        0 = Zero-scale (wiper contact resistance)
        50 = Midscale
        >=100 = Full scale
        """
        self._validate_channel(channel)
        self._write(channel, int((value * 255)/100))


class AD8400(AD840X):
    """AD8400-based digital potentiometer class with 1 potentiometer."""
    CHANNELS = 0

class AD8402(AD840X):
    """AD8402-based digital potentiometer class with 2 potentiometer."""
    CHANNELS = 1

class AD8403(AD840X):
    """AD8403-based digital potentiometer class with 3 potentiometer."""
    CHANNELS = 3
