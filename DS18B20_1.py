""" DS18B20. Mostra la temperatura """

# importa mòduls:
import onewire, ds18x20    # per interactuar amb el sensor DS18B20
from machine import Pin    # per interactuar amb els GPIO
from time import sleep     # per definir pauses

# creació d'objecte ds18x20 associat al pin de connexió del sensor:
sensor = ds18x20.DS18X20(onewire.OneWire(Pin(4)))

# cerca l'objecte definit i desa la seva adreça dins la variable adreces, que té format de llista:
adreces = sensor.scan()                  
print('Trobat dispositiu DS: ', adreces)    # mostra l'adreça o adreces trobades

while True:
    sensor.convert_temp()     # llegeix el sensor i converteix les dades
    sleep (0.75)              # cal donar temps a realitzar l'acció anterior
    for i in adreces:         # per a cada element de la llista roms ...
        #print (i)            # això mostra l'adreça del dispositiu ds_sensor
        #print (sensor.read_temp(i))             # mostra la temperatura
        print ('T=', sensor.read_temp(i), 'ºC')  # mostra la temperatura: magnitud, valor i unitat
    sleep (5)                 # interval d'actualització: 5 segons 
