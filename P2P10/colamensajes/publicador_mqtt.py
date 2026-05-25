import paho.mqtt.client as mqtt
import time
import random

# Configuración del cliente MQTT
client = mqtt.Client("publicador_temperatura")

client.connect("localhost", port=1883)
client.loop_start()

try:
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        mensaje = f"Temperatura: {temp} °C"

        # Publica con QoS 1
        client.publish("sensor/cola", mensaje, qos=1)

        print("📤 Mensaje enviado:", mensaje)

        time.sleep(5)

except KeyboardInterrupt:
    print("🛑 Publicador detenido.")

client.loop_stop()
