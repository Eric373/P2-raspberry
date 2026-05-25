import sqlite3
import time

# Conexión a SQLite en RAM (nueva instancia: no compartirá datos con el publicador)
# conn = sqlite3.connect(":memory:")  # Esto reinicia los datos
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

print("🕓 Esperando mensajes en SQLite RAM...")

try:
    while True:
        cursor.execute(
            "SELECT id, mensaje FROM cola ORDER BY id ASC LIMIT 1"
        )

        mensaje = cursor.fetchone()

        if mensaje:
            print("📥 Mensaje recibido:", mensaje[1])

            cursor.execute(
                "DELETE FROM cola WHERE id = ?",
                (mensaje[0],)
            )

            conn.commit()

        else:
            time.sleep(2)

except KeyboardInterrupt:
    print("🛑 Subscriptor detenido.")

conn.close()
