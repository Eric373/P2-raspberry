# subscriber_qos1.py

import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[QoS 1] Mensaje recibido: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"SubQoS1")
client.on_message = on_message

client.connect("localhost")
client.subscribe("sala/humedad", qos=1)

client.loop_start()

input("Presiona Enter para salir...\n")

client.loop_stop()
client.disconnect()
