import board

# Pines
I2C_SCL = board.SCL
I2C_SDA = board.SDA
DHT_PIN = board.D17

# Pantalla
OLED_WIDTH = 128
OLED_HEIGHT = 64

# Parámetros
TEMP_MAX = 50
HUM_MAX = 100
HIST_MAX_POINTS = 128
REFRESH_DELAY = 2  # segundos
ANIM_LIMIT = 2

# Rutas de íconos
ICON_TEMP_PATH = "icons/temp.bmp"
ICON_HUM_PATH = "icons/hum.bmp"
