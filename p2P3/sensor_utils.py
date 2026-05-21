import adafruit_dht
import board
import time

class DHT11Sensor:
    def __init__(self, pin=board.D4):
        # Inicializa el sensor en el pin especificado (por defecto GPIO4)
        self.sensor = adafruit_dht.DHT11(board.D17)

    def read(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity
            
            if temperature is None or humidity is None:
                raise ValueError("Valores nulos recibidos")
            
            return temperature, humidity

        except RuntimeError as e:
            # Los errores RuntimeError son comunes con DHT11 (errores de lectura)
            # Simplemente devolvemos None y dejamos que el programa principal decida qué hacer
            return None, None
            
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None, None

    def close(self):
        # Libera el pin GPIO
        self.sensor.exit()

# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Instanciamos la clase
    dht_sensor = DHT11Sensor(board.D4)
    
    try:
        while True:
            temp, hum = dht_sensor.read()
            
            if temp is not None:
                print(f"Temp: {temp:.1f}°C | Humedad: {hum}%")
            else:
                print("Error de lectura, intentando de nuevo...")
            
            # El DHT11 necesita al menos 2 segundos entre lecturas
            time.sleep(2.0)
            
    except KeyboardInterrupt:
        print("\nCerrando sensor...")
    finally:
        dht_sensor.close()
