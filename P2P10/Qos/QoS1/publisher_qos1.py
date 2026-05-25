# publisher_qos1.py

import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"PubQoS1")
client.connect("localhost")

mensaje = "Humedad: 60%"

client.publish("sala/humedad", mensaje, qos=1)

print("[QoS 1] Publicado:", mensaje)

client.disconnect()
