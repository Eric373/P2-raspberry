from RPLCD.i2c import CharLCD

class LCD:
    def __init__(self, address=0x27, port=1):
        self.lcd = CharLCD('PCF8574', address, port=port,
                           cols=16, rows=2, charmap='A00',
                           auto_linebreaks=True)

    def clear(self):
        self.lcd.clear()

    def write(self, line1='', line2=''):
        self.clear()
        self.lcd.write_string(line1[:16])
        if line2:
            self.lcd.cursor_pos = (1, 0)
            self.lcd.write_string(line2[:16])
            
    def close(self):
        self.lcd.close()
