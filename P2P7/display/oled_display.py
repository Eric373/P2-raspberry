from PIL import Image, ImageDraw, ImageFont
import board
import busio
import adafruit_ssd1306
import time
import os


class OLEDDisplay:
    def __init__(self, width=128, height=64):
        i2c = busio.I2C(board.SCL, board.SDA)

        self.disp = adafruit_ssd1306.SSD1306_I2C(
            width,
            height,
            i2c
        )

        self.width = width
        self.height = height

        self.disp.fill(0)
        self.disp.show()

        self.font = ImageFont.load_default()

        self.load_icons()

    def load_icons(self):
        base = os.path.dirname(__file__)

        self.temp_icon = Image.open(
            os.path.join(base, "icons", "temp.png")
        ).resize((16, 16)).convert("1")

        self.hum_icon = Image.open(
            os.path.join(base, "icons", "humedad.png")
        ).resize((16, 16)).convert("1")

    def update(self, temperature, humidity):
        image = Image.new("1", (self.width, self.height))
        draw = ImageDraw.Draw(image)

        image.paste(self.temp_icon, (0, 0))
        draw.text(
            (20, 0),
            f"{temperature}°C",
            font=self.font,
            fill=255
        )

        image.paste(self.hum_icon, (0, 20))
        draw.text(
            (20, 20),
            f"{humidity}%",
            font=self.font,
            fill=255
        )

        self.disp.image(image)
        self.disp.show()
