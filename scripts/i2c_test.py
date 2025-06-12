import ssd1306
#import tcs34725
import time
from machine import I2C, Pin, ADC

# Define I2C
i2c = I2C(scl=Pin(22), sda=Pin(23), freq=100000)

# Define oled
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
oled.fill(0)

# Define rgb sensor
#sensor = tcs34725.TCS34725(i2c)
#sensor.integration_time(10) #value between 2.4 and 614.4.
#sensor.gain(16) #must be a value of 1, 4, 16, 60

#Defining the phototransistor sensor
photo_adc = ADC(Pin(32, Pin.PULL_DOWN))
photo_adc.atten(ADC.ATTN_11DB)  
  

def color_rgb_bytes(color_raw): #This code is only used for rgb sensor
    """Read the RGB color detected by the sensor.  Returns a 3-tuple of
    red, green, blue component values as bytes (0-255).
    NOTE: These values are normalized against 'clear', remove the division
    by 'clear' if you need the raw values.
    """
    r, g, b, clear = color_raw
    # Avoid divide by zero errors ... if clear = 0 return black
    if clear == 0:
        return (0, 0, 0)
    red   = int(pow((int((r/clear) * 256) / 255), 2.5) * 255)
    green = int(pow((int((g/clear) * 256) / 255), 2.5) * 255)
    blue  = int(pow((int((b/clear) * 256) / 255), 2.5) * 255)
    # Handle possible 8-bit overflow
    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue > 255:
        blue = 255
    return (red, green, blue)

while True:
    # Read color sensor
    #r,g,b = color_rgb_bytes(sensor.read(True))
    # Read the OD sensor
    light_val = photo_adc.read()


    # Show results on OLED
    oled.fill(0)
    #oled.text('R: {}'.format(r), 0, 8)
    #oled.text('G: {}'.format(g), 0, 16)
    #oled.text('B: {}'.format(b), 0, 24)
    oled.text('Light:', 0, 10)
    oled.text(str(light_val), 0, 20)
    oled.show()

    # Print results
    #answer = '>r:{} g:{} b:{}<'.format(r, g, b)
    #print(answer, end='\n')
    print("Phototransistor Reading: ", light_val)

    # Wait 1 second before repeating
    time.sleep(1)

