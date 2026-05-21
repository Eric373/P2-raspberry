import os
import requests
from PIL import Image
from io import BytesIO

urls = {
    "temp.bmp": "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/256/thermometer-half.png",
    "hum.bmp": "https://raw.githubusercontent.com/encharm/Font-Awesome-SVG-PNG/master/black/png/256/tint.png"
}

for nombre, url in urls.items():
    print(f"Arreglando {nombre}...")
    respuesta = requests.get(url)

    # 1. Abrimos la imagen respetando su canal de transparencia (RGBA)
    img = Image.open(BytesIO(respuesta.content)).convert("RGBA")

    # 2. El truco: separamos las capas y nos quedamos SOLO con el canal Alpha (la transparencia)
    # Esto nos regala una silueta 100% blanca sobre un fondo negro.
    silueta_blanca = img.split()[3] 

    # 3. Redimensionamos a 24x24, pasamos a 1-bit y sobrescribimos el archivo malo
    silueta_blanca.resize((24, 24)).convert("1").save(f"icons/{nombre}")

print("¡Íconos arreglados perfectamente!")
