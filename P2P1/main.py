import time
import busio
from config import *
from sensor_dht import SensorDHT
from oled_visualizer import OledVisualizer

def main():
    i2c = busio.I2C(I2C_SCL, I2C_SDA)
    visual = OledVisualizer(i2c)
    sensor = SensorDHT()

    temp_hist = []
    hum_hist = []

    try:
        while True:
            temp, hum = sensor.leer()
            if temp is not None and hum is not None:
                temp_hist.append(temp)
                hum_hist.append(hum)

                if len(temp_hist) > HIST_MAX_POINTS:
                    temp_hist.pop(0)
                    hum_hist.pop(0)

                visual.mostrar_datos(temp, hum, temp_hist, hum_hist)
            else:
                print("Saltando actualización por error de lectura.")

            time.sleep(REFRESH_DELAY)

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")

    except Exception as e:
        print(f"Error inesperado: {e}")

    finally:
        sensor.cerrar()

if __name__ == "__main__":
    main()
