from collections import deque
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import time
import json

from datetime import datetime

GPIO_PIN = board.D17

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/dht"
MQTT_QoS = 1

INTERVALO_LECTURA = 5

cola_mensajes = deque()

def leer_dht(sensor, intentos=5, delay=2):
    for intento in range(intentos):
        try:
            t = sensor.temperature
            h = sensor.humidity

            if t is not None and h is not None:
                return t, h

        except RuntimeError as e:
            print(f"[{intento+1}/{intentos}] Lectura fallida: {e}")
            time.sleep(delay)

    raise RuntimeError("No se pudo leer del sensor.")

def on_connect(client, userdata, flags, rc):
    print(
        "[MQTT] Conectado."
        if rc == 0
        else f"[MQTT] Error de conexión: {rc}"
    )

def on_publish(client, userdata, mid):
    print(f"[MQTT] Publicación confirmada. MID: {mid}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_publish = on_publish

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

dht_sensor = adafruit_dht.DHT11(GPIO_PIN)

while True:
    try:
        temp, hum = leer_dht(dht_sensor)

        timestamp = datetime.now().isoformat()

        mensaje = json.dumps({
            "timestamp": timestamp,
            "temperatura": temp,
            "humedad": hum
        })

        cola_mensajes.append(mensaje)

        for _ in range(len(cola_mensajes)):
            actual = cola_mensajes[0]

            result = client.publish(
                MQTT_TOPIC,
                actual,
                MQTT_QoS
            )

            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                print("📤 Enviado:", actual)
                cola_mensajes.popleft()

            else:
                print("⚠️ Publicación fallida. Reintentando...")
                break

    except Exception as e:
        print("[Error]", e)

    time.sleep(INTERVALO_LECTURA)
