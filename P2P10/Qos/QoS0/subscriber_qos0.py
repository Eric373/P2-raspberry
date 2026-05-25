import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"[QoS 0] Mensaje recibido: {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1,"SubQoS0")
client.on_message = on_message

client.connect("localhost")
client.subscribe("sala/temperatura", qos=0)

client.loop_start()

input("Presiona Enter para salir...\n")

client.loop_stop()
client.disconnect()
