import paho.mqtt.client as mqtt

# Configuración del subscriptor persistente
client = mqtt.Client(
    client_id="subscriptor_temperatura",
    clean_session=False
)

# Conexión al broker
def on_connect(client, userdata, flags, rc):
    print("✅ Conectado al broker")

    # Nos suscribimos al topic con QoS 1
    client.subscribe("sensor/cola", qos=1)

# Recepción de mensajes
def on_message(client, userdata, msg):
    print("📥 Mensaje recibido desde la cola:", msg.payload.decode())

client.on_connect = on_connect
client.on_message = on_message

# Conectar al broker y mantener sesión
client.connect("localhost", port=1883)

client.loop_forever()
