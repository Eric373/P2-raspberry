# publisher_qos2.py

import paho.mqtt.client as mqtt

client = mqtt.Client("PubQoS2")
client.connect("localhost")

client.loop_start()
mensaje = "Alerta: Nivel de gas elevado"

info = client.publish("sala/gas", mensaje, qos=2)
info.wait_for_publish()
print("[QoS 2] Publicado:", mensaje)

client.loop_stop()
client.disconnect()
