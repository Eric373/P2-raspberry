import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
topic = "iot/qos/temp"
qos_level = 1  # Cambia entre 0, 1 o 2

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"RaspberryPiQoSPub")
client.connect(broker)

try:
    while True:
        temp = round(random.uniform(20, 30), 2)

        client.publish(topic, f"{temp}", qos=qos_level)
        print(f"Publicado con QoS {qos_level}: {temp} °C")

        time.sleep(2)

except KeyboardInterrupt:
    print("Publicador detenido")
    client.disconnect()
