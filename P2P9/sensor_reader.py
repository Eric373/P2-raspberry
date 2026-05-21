import adafruit_dht
import board
import time

from typing import Tuple, Optional


class DHT11Reader:
    def __init__(self, gpio_pin=board.D17):
        self.sensor = adafruit_dht.DHT11(gpio_pin)

    def read(self) -> Optional[Tuple[float, float]]:
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity

            if (
                temperature is not None and
                humidity is not None
            ):
                return temperature, humidity

        except RuntimeError as e:
            print(
                f"[DHT11Reader] Error de lectura: {e}"
            )

        return None
