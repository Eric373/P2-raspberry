import redis
import time
import random

# Conexión a Redis
r = redis.Redis(host='localhost', port=6379, db=0)

try:
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        mensaje = f"Temperatura: {temp} °C"

        r.rpush("cola:temperatura", mensaje)

        print("📤 Encolado:", mensaje)

        time.sleep(5)

except KeyboardInterrupt:
    print("🛑 Publicador detenido.")
