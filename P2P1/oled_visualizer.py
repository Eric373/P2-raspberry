import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont, ImageOps
from config import *
from utils import escalar

class OledVisualizer:
    def __init__(self, i2c, width=OLED_WIDTH, height=OLED_HEIGHT, icon_temp_path=ICON_TEMP_PATH, icon_hum_path=ICON_HUM_PATH):
        self.display = adafruit_ssd1306.SSD1306_I2C(width, height, i2c)
        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()
        self.icon_temp = Image.open(icon_temp_path).convert("1")
        self.icon_hum = Image.open(icon_hum_path).convert("1")
        self.anim_offset = 0
        self.anim_dir = 1

    def actualizar_animacion(self):
        self.anim_offset += self.anim_dir
        if abs(self.anim_offset) >= ANIM_LIMIT:
            self.anim_dir *= -1

    def limpiar(self):
        self.draw.rectangle((0, 0, OLED_WIDTH, OLED_HEIGHT), outline=0, fill=0)

    def mostrar_datos(self, temp, hum, temp_hist, hum_hist):
        self.limpiar()
        self.actualizar_animacion()

        # Íconos animados
        self.image.paste(self.icon_temp, (0, 0 + self.anim_offset))
        self.image.paste(self.icon_hum, (0, OLED_HEIGHT - 16 - self.anim_offset))

        # Texto
        self.draw.text((20, 0), f"{temp:.1f} C", font=self.font, fill=255)
        self.draw.text((20, OLED_HEIGHT - 12), f"{hum:.1f} %", font=self.font, fill=255)

        # Gráficas
        self._dibujar_historial(temp_hist, TEMP_MAX, 24, 12)
        self._dibujar_historial(hum_hist, HUM_MAX, 24, 35)

        self.display.image(self.image)
        self.display.show()

    def _dibujar_historial(self, datos, valor_max, alto, offset_y):
        for i in range(1, len(datos)):
            x1, x2 = i - 1, i
            y1 = escalar(datos[i - 1], valor_max, alto) + offset_y
            y2 = escalar(datos[i], valor_max, alto) + offset_y
            self.draw.line((x1, y1, x2, y2), fill=255)
