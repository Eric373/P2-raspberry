# oled_display.py

import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

from config import (
    I2C_ADDRESS,
    WIDTH,
    HEIGHT,
    SCROLL_SPEED,
    MESSAGE
)


class OLEDScroller:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)

        self.display = adafruit_ssd1306.SSD1306_I2C(
            WIDTH,
            HEIGHT,
            self.i2c,
            addr=I2C_ADDRESS
        )

        self.display.fill(0)
        self.display.show()

        # Doble ancho para scrolling
        self.image = Image.new("1", (WIDTH * 2, HEIGHT))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

    # Hay un error en la función textsize().
    # En versiones recientes de Pillow (>= 10.0.0),
    # el método textsize() fue eliminado y reemplazado
    # por textbbox() o textlength().
    def scroll_textOLD(self, text):
        self.draw.rectangle(
            (0, 0, WIDTH * 2, HEIGHT),
            outline=0,
            fill=0
        )

        self.draw.text(
            (0, 0),
            text,
            font=self.font,
            fill=255
        )

        text_width, _ = self.draw.textsize(
            text,
            font=self.font
        )

        for x in range(0, text_width + 1):
            cropped = self.image.crop(
                (x, 0, x + WIDTH, HEIGHT)
            )

            self.display.image(cropped)
            self.display.show()
            time.sleep(SCROLL_SPEED)

    # Versión corregida de la función
    def scroll_text(self, text):
        self.draw.rectangle(
            (0, 0, WIDTH * 2, HEIGHT),
            outline=0,
            fill=0
        )

        self.draw.text(
            (0, 0),
            text,
            font=self.font,
            fill=255
        )

        bbox = self.draw.textbbox(
            (0, 0),
            text,
            font=self.font
        )

        text_width = bbox[2] - bbox[0]

        for x in range(0, text_width + 1):
            cropped = self.image.crop(
                (x, 0, x + WIDTH, HEIGHT)
            )

            self.display.image(cropped)
            self.display.show()
            time.sleep(SCROLL_SPEED)

    def clear(self):
        self.display.fill(0)
        self.display.show()
