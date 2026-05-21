from sensor import DHT11Sensor
from display import LCDDisplay
from utils import delay

def main():
    sensor = DHT11Sensor()
    lcd = LCDDisplay()
    
    while True:
        temp, hum = sensor.read_data()
        
        if temp is not None and hum is not None:
            lcd.show_message(f"T:{temp}C", f"H:{hum}%")
        else:
            lcd.show_message("Sensor", "sin lectura")
            
        delay(2)

if __name__ == "__main__":
    main()
