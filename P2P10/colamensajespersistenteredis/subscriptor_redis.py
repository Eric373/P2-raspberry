import redis
import time

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

print("🕓 Esperando mensajes...")

try:
    while True:
        # Espera bloqueante por nuevos mensajes
        _, mensaje = r.blpop("cola:temperatura")

        print("📥 Mensaje recibido:", mensaje.decode())

except KeyboardInterrupt:
    print("🛑 Subscriptor detenido.")
