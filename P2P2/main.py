import time
from lcd_display import LCD

def main():
    lcd = LCD()
    try:
        lcd.write("Javielquelolea", "LCD I2C OK")
        time.sleep(5)
        lcd.write("Raspberry Pi", "con LCD I2C")
        time.sleep(5)
        lcd.clear()
    except KeyboardInterrupt:
        print("Interrupción del usuario.")
    finally:
        lcd.close()
        print("LCD apagado correctamente.")

if __name__ == "__main__":
    main()
