from display_manager import OLEDDisplay
from utils import get_timestamp
import time


def main():
    oled = OLEDDisplay()

    oled.show_text("Inicializando...")
    time.sleep(1)

    # Mostrar logo (opcional)
    oled.show_logo("assets/logo.pbm")
    time.sleep(30)

    try:
        while True:
            now = get_timestamp()
            oled.show_text(f"Hora:\n{now}")
            time.sleep(1)

    except KeyboardInterrupt:
        oled.clear()
        print("Programa finalizado.")


if __name__ == "__main__":
    main()
