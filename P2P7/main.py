import time

from sensors.dht11_reader import DHT11Reader
from display.oled_display import OLEDDisplay


def main():
    sensor = DHT11Reader()
    display = OLEDDisplay()

    while True:
        temp, hum = sensor.read()

        if temp is not None and hum is not None:
            display.update(temp, hum)

        time.sleep(2)


if __name__ == "__main__":
    main()
