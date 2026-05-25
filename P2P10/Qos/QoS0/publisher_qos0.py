import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"PubQoS0")
client.connect("localhost")

mensaje = "Temp: 24.5 °C"

client.publish("sala/temperatura", mensaje, qos=0)

print("[QoS 0] Publicado:", mensaje)

client.disconnect()
