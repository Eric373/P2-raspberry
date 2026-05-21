# main.py
from lcd_utils import LCDController

def main():
    lcd = LCDController()
    try:
        lcd.clear()
        lcd.write("LCD Inicializado", line=0)
        lcd.scroll_text(
            "Este texto se desplaza hacia la izquierda!", 
            line=1,
            delay=0.2, 
            repeat=3
        )
    except Exception as e:
        print(f"Error: {e}")
    finally:
        lcd.close()

if __name__ == "__main__":
    main()
