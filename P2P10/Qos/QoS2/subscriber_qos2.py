# subscriber_qos2.py

import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[QoS 2] Mensaje recibido: {msg.payload.decode()}")

client = mqtt.Client("SubQoS2")
client.on_message = on_message

client.connect("localhost")
client.subscribe("sala/gas", qos=2)

client.loop_start()

input("Presiona Enter para salir...\n")

client.loop_stop()
client.disconnect()
