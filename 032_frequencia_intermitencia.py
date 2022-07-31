""" Control de la freqüència d'intermitència d'un LED amb potenciòmetre """

# importa llibreries
from machine import Pin, ADC,
from time import sleep

# definició d'objectes
led = Pin(23, Pin.OUT)
sensor = ADC (Pin(32))
sensor.width (ADC.WIDTH_10BIT)      # ajust de la resolució per obtenir valors entre 0 i 1023

# execució contínua
while True:
  valor_sensor = sensor.read()      # llegeix l'entrada analògica (valors entre 0 i 1023)
  pausa = valor_sensor/1000         # divideixo entre 1000 perquè la pausa ha de ser en segons
  led.on()                          # encén el led
  sleep(pausa)                      # durant el temps corresponent a la lectura del sensor
  led.off()                         # apaga el led
  sleep(pausa)
