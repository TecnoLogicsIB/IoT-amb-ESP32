""" Lectura dels valors d'un sensor analògic """

# importa llibreries:
from machine import Pin, ADC     # importa les classes Pin i ADC de la llibreria machine
from time import sleep           # importa la classe sleep de la llibreria time per poder definir pauses

# configuració:
sensor = ADC (Pin (32))          # crea l'objecte ADC que he anomenat sensor al pin 32
sensor.width (ADC.WIDTH_10BIT)   # si cal: ajust de la resolució (10 bits: valors de 0 a 1023)
sensor.atten (ADC.ATTN_11DB)     # si cal: ajust del rang de lectura (tot el rang de 0 a 3.3V)

# execució contínua:
while True:
    print (sensor.read())        # mostra la lectura del senyal al pin del sensor
    sleep(0.1)                   # pausa de 0.1 s (100 ms)
