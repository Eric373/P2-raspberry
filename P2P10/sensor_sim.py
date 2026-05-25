import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
topic = "iot/temperatura"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"RaspberryPiPublisher")
client.connect(broker)

try:
    while True:
        temperatura = round(random.uniform(20.0, 30.0), 2)
        
        client.publish(topic, f"{temperatura}")
        print(f"Publicado: {temperatura} °C")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("Publicador detenido")
    client.disconnect()
