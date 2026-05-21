import time

from sensor_reader import DHT11Reader
from plotter import LivePlotter


def main():
    sensor = DHT11Reader()
    plotter = LivePlotter()

    start_time = time.time()

    print(
        "Iniciando lectura... "
        "Presiona Ctrl+C para detener."
    )

    try:
        while True:
            data = sensor.read()

            if data:
                elapsed_time = round(
                    time.time() - start_time,
                    1
                )

                temperature, humidity = data

                print(
                    f"[{elapsed_time}s] "
                    f"Temp: {temperature}°C | "
                    f"Humedad: {humidity}%"
                )

                plotter.update(
                    elapsed_time,
                    temperature,
                    humidity
                )

            # DHT11 requiere tiempo entre lecturas
            time.sleep(2)

    except KeyboardInterrupt:
        print(
            "\n[INFO] Lectura finalizada por el usuario."
        )

    except Exception as e:
        print(f"[ERROR] {e}")

    finally:
        print("[INFO] Cerrando aplicación.")


if __name__ == "__main__":
    main()
