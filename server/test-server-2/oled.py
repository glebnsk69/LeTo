print("="*16,"start main.py","="*16)

import gc
from machine import Pin, I2C
import ssd1306
from time import sleep_ms

i2c = I2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

def oledPrint(text):
    print(test)
    oled.scroll(0,16)
    oled.text(text)
    oled.show()

gc.collect()

for i in range(10):
    oledPrint('Line #',i)
    sleem_ms(500)
