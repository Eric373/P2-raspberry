# lcd_utils.py
from RPLCD.i2c import CharLCD
import time

class LCDController:
    def __init__(self, address=0x27, cols=16, rows=2):
        self.lcd = CharLCD(
            i2c_expander='PCF8574', 
            address=address,
            port=1, 
            cols=cols, 
            rows=rows, 
            charmap='A00',
            auto_linebreaks=True
        )
        self.cols = cols
        self.rows = rows

    def clear(self):
        self.lcd.clear()

    def write(self, text, line=0):
        self.lcd.cursor_pos = (line, 0)
        self.lcd.write_string(text.ljust(self.cols))

    def scroll_text(self, text, line=0, delay=0.3, repeat=1):
        scroll_text = text + " " * self.cols
        for _ in range(repeat):
            for i in range(len(scroll_text) - self.cols + 1):
                self.write(scroll_text[i:i+self.cols], line)
                time.sleep(delay)

    def close(self):
        self.lcd.close(clear=True)
