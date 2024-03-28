#Declaration of libraries and files
from machine import Pin, I2C, ADC,PWM
import machine
import utime
from utime import sleep_ms, sleep
import time
from neopixel import Neopixel
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

uart = machine.UART(0, tx = machine.Pin(0), rx = machine.Pin(1), baudrate=115200)
uart.init(115200, bits = 8, parity = None, stop = 1)# El número 0 suele ser el UART predeterminado en la mayoría de los dispositivos


if __name__ == '__main__':
    
    
    i2c = I2C(0, sda=Pin(4), scl=Pin(3), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    
    sleep_ms(1000)
  
    #Assign input and output pins
    sensor = ADC(4)
    strip = Neopixel(8, 0, 1, "RGB")
    #buz = PWM(Pin(13))
    buz = Pin(2,Pin.OUT)
    pot = ADC(0)
    i2c = I2C(1, scl = Pin(15), sda = Pin(14), freq = 200000)
    btn = Pin(13, Pin.IN)
    
    voltaje_12_25 = True
    
    if(voltaje_12_25 == True):
        #Volatje de 25 volts
        val = pot.read_u16()
        #Factor para converitr la entrada del divisor de volatje a voltaje
        FACTOR = (3.3/ (65535)) * 0.0003845
    else:
        #Voltaje de 12 volts
        val = pot.read_u16()
        #Factor para converitr la entrada del divisor de volatje a voltaje
        FACTOR = (3.3/ (65535)) * 0.0003845
    
    
        
    
    #Declaration of colors to Neopixels
    red = (0, 255, 0)
    orange = (255, 120, 0)
    yellow = (255, 255, 0)
    green = (255, 0, 0)
    blue = (0, 0, 255)
    violet = (138, 43, 226)
    none = (0,0,0)
    colors_rgb = (red, orange, yellow, green, blue, violet)

    #Set brightness if Neopixels
    strip.brightness(85)
    


    def boton_interrupt(pin):
      #valor que entra del sensor interno  de temperatura
        valor = sensor.read_u16()*3.3/65635
      #imprime el valor de temperatura en la lcd cuando presionas el boton
        temp = str(round((27-(valor-0.706)/0.001721),2))
        lcd.putstr(f"temperatura: {temp} ")

    btn.irq(trigger =Pin.IRQ_RISING, handler = boton_interrupt)
 
 
    while True:
        #actualiza cada segundo
        lcd.putstr(f"Quantum Robotics  \n   TEC CEM")
        lcd.clear()
        sleep_ms(1000)
        prom = 500
        cont = 0
        #sacar el promedio de los valores del divisor de volatje cada 500 mediciones
        for i in range(prom):
            
        cont = cont+val
        valo = cont/prom
        #calculo del promedio por el factor
        volts = valo * FACTOR
        #redondea a 2 puntos decimales
        a = str(round(volts,2))
        lcd.putstr("voltaje: {a}")
        uart.write(a)
        
        
        if(voltaje_12_25 == True):
            if (volts >25.0 and volts <= 25.2):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, green)
                strip.set_pixel(6, green)
                strip.set_pixel(7, green)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
            if (volts >24.8 and volts <= 25.0):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, green)
                strip.set_pixel(6, green)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >24.6 and volts <= 24.8):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, green)
                strip.set_pixel(6, yellow)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)           
            if (volts >24.4 and volts <= 24.6):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, yellow)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >24.2 and volts <= 24.4):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, yellow)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >24.0 and volts <= 24.2):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, yellow)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >23.8 and volts <= 24.0):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, yellow)
                strip.set_pixel(3, red)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >23.6 and volts <= 23.8):
                strip.set_pixel(0, green)
                strip.set_pixel(1, yellow)
                strip.set_pixel(2, red)
                strip.set_pixel(3, red)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
            
            if (volts <= 23.4):
                strip.set_pixel(0, red)
                strip.set_pixel(1, red)
                strip.set_pixel(2, red)
                strip.set_pixel(3, red)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                buz.on()
                time.sleep(1)
                buz.off()
                sleep_ms(3000)
            
        if(voltaje_12_25 == False):
            if (volts >12.0 and volts <= 12.2):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, green)
                strip.set_pixel(6, green)
                strip.set_pixel(7, green)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >11.8 and volts <= 12.0):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, green)
                strip.set_pixel(6, green)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >11.6 and volts <= 11.8):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, green)
                strip.set_pixel(6, yellow)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                                
            if (volts >11.4 and volts <= 11.6):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, green)
                strip.set_pixel(5, yellow)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >11.2 and volts <= 11.4):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, green)
                strip.set_pixel(4, yellow)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >11.0 and volts <= 11.2):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, green)
                strip.set_pixel(3, yellow)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >10.8 and volts <= 11.0):
                strip.set_pixel(0, green)
                strip.set_pixel(1, green)
                strip.set_pixel(2, yellow)
                strip.set_pixel(3, red)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
                
            if (volts >10.6 and volts <= 10.8):
                strip.set_pixel(0, green)
                strip.set_pixel(1, yellow)
                strip.set_pixel(2, red)
                strip.set_pixel(3, red)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                sleep_ms(3000)
            
            if (volts <= 10.4):
                strip.set_pixel(0, red)
                strip.set_pixel(1, red)
                strip.set_pixel(2, red)
                strip.set_pixel(3, red)
                strip.set_pixel(4, red)
                strip.set_pixel(5, red)
                strip.set_pixel(6, red)
                strip.set_pixel(7, red)
                time.sleep(0.01)
                strip.show()
                buz.on()
                time.sleep(1)
                buz.off()
                sleep_ms(3000)
                