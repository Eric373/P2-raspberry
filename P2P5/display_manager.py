import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont


class OLEDDisplay:
    def __init__(self, width=128, height=64):
        self.width = width
        self.height = height

        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.display = adafruit_ssd1306.SSD1306_I2C(
            width,
            height,
            self.i2c
        )

        self.display.fill(0)
        self.display.show()

        self.image = Image.new("1", (width, height))
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.load_default()

    def clear(self):
        self.draw.rectangle(
            (0, 0, self.width, self.height),
            outline=0,
            fill=0
        )

    def show_text(self, text, x=0, y=0):
        self.clear()
        self.draw.text(
            (x, y),
            text,
            font=self.font,
            fill=255
        )
        self.display.image(self.image)
        self.display.show()

    def show_logo(self, path):
        self.clear()

        logo = Image.open(path).convert("1").resize(
            (self.width, self.height)
        )

        self.display.image(logo)
        self.display.show()
