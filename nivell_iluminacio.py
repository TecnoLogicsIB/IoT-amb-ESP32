""" Control del nivell d'il·luminació d'un LED amb potenciòmetre """

# importa llibreries
from machine import Pin, ADC, PWM
from time import sleep

# definició d'objectes
led = PWM (Pin(23), freq=5000)
sensor = ADC (Pin(32))
sensor.width (ADC.WIDTH_10BIT)  # per obtenir valors entre 0 i 1023

# execució contínua
while True:
  valor_sensor = sensor.read()  # llegeix l'entrada analògica (valors entre 0 i 1023)
  led.duty (valor_sensor)       # assigna nivell d'il·luminació (0 a 1023) segons valor sensor (0 a 1023)
  sleep(.1)