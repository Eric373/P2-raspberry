import adafruit_dht
import board
import time


class DHT11Reader:
    def __init__(self, pin=board.D17):
        self.sensor = adafruit_dht.DHT11(pin)

    def read(self):
        try:
            temp = self.sensor.temperature
            hum = self.sensor.humidity

            return temp, hum

        except RuntimeError:
            return None, None
