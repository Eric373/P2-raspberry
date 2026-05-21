import time

def delay(seconds):
    try:
        time.sleep(seconds)
    except KeyboardInterrupt:
        print("Interrupción del usuario.")
