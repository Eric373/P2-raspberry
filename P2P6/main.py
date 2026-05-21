from oled_display import OLEDScroller
from config import MESSAGE


def main():
    scroller = OLEDScroller()

    while True:
        scroller.scroll_text(MESSAGE)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("\nEjecución finalizada por el usuario.")
