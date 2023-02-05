""" Programa senzill per mostrar la temperatura si només utilitzem 1 sensor DS18B20 """

# importa mòduls:
import onewire, ds18x20    # per interactuar amb el sensor DS18B20
from machine import Pin    # per interactuar amb els GPIO
from time import sleep     # per definir pauses

# creació d'objecte ds18x20 associat al pin de connexió del sensor:
sensor = ds18x20.DS18X20(onewire.OneWire(Pin(4)))

# cerca l'objecte definit i desa la seva adreça dins la variable adreça, que té format de llista:
adreça = sensor.scan()                  
print('Trobat dispositiu DS: ', adreça)    # mostra l'adreça trobada

while True:
    sensor.convert_temp()     # llegeix el sensor i converteix les dades
    sleep (0.75)              # cal donar temps a realitzar l'acció anterior
    # variable per desar la temperatura llegida pel sensor:
    temperatura = sensor.read_temp(adreça[0])  # tot i que només hi hagi un element, la variable adreça té format de lista
    # mostra les temperatures (magnitud, valor i unitat):
    print ('T=', temperatura, 'ºC')      
    sleep (5)                 # interval d'actualització: 5 segons
