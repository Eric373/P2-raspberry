from sensor_utils import DHT11Sensor
import time
def read_sensor_continuous(interval=2, iterations=10):
	sensor = DHT11Sensor()
	try:
		for i in range(iterations):
			temperature, humidity = sensor.read()
			if temperature is not None:
				print(f"[{i+1}] Temp: {temperature:.1f}°C Hum: {humidity:.1f}%")
			else:
				print(f"[{i+1}] Error al leer el sensor.")
			time.sleep(interval)
	finally:
		sensor.close()
