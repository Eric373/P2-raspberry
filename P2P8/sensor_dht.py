import adafruit_dht

from config import DHT_PIN


class SensorDHT:
    def __init__(self, pin=DHT_PIN):
        self.dht = adafruit_dht.DHT11(pin)

    def leer(self):
        try:
            temp = self.dht.temperature
            hum = self.dht.humidity

            if temp is not None and hum is not None:
                return temp, hum
            else:
                raise ValueError("Lectura inválida del sensor.")

        except RuntimeError as e:
            print("Error de lectura DHT11:", e.args[0])
            return None, None

    def cerrar(self):
        self.dht.exit()
