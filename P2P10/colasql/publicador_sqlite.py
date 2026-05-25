import sqlite3
import time
import random

# Conexión a SQLite en RAM (nueva instancia: no compartirá datos con el publicador)
# conn = sqlite3.connect(":memory:")  # crea los datos en RAM
# cursor = conn.cursor()

# Para simular persistencia entre procesos, usamos SQLite en DISCO:
conn = sqlite3.connect("mensajes.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS cola (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mensaje TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Insertar mensajes en la cola
try:
    while True:
        temp = round(random.uniform(20.0, 30.0), 2)
        mensaje = f"Temperatura: {temp} °C"

        cursor.execute(
            "INSERT INTO cola (mensaje) VALUES (?)",
            (mensaje,)
        )

        conn.commit()

        print("📤 Encolado:", mensaje)

        time.sleep(5)

except KeyboardInterrupt:
    print("🛑 Publicador detenido.")

conn.close()
