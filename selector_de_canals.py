""" Selector de canals """

# importa llibreries
from machine import Pin, ADC
from time import sleep

# definició d'objectes
led1 = Pin(23, Pin.OUT)
led2 = Pin(21, Pin.OUT)
sensor = ADC (Pin(34))
sensor.width (ADC.WIDTH_10BIT)  # per obtenir valors entre 0 i 1023

# execució contínua
while True:
  valor_sensor = sensor.read() # llegeix l'entrada analògica
  print(valor_sensor)
  
  if valor_sensor < 500:
    led1.on()
    led2.off()
  else:
    led1.off()
    led2.on()
  sleep(.1)