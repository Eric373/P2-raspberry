from PIL import Image

# Cargar la imagen que acabamos de descargar y convertirla a 1 bit (blanco y negro)
img = Image.open("logo_original.png").convert("1")

# Redimensionar al tamaño exacto de la pantalla OLED
img = img.resize((128, 64))

# Guardar la imagen convertida dentro de la carpeta assets
img.save("assets/logo.pbm")

print("¡Imagen generada con éxito en assets/logo.pbm!")
