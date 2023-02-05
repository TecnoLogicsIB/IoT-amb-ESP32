""" DS18B20. Mostra la temperatura """

# importa mòduls:
import onewire, ds18x20    # per interactuar amb el sensor DS18B20
from machine import Pin    # per interactuar amb els GPIO
from time import sleep     # per definir pauses

# creació d'objecte ds18x20 associat al pin de connexió del sensor:
ds_sensor = ds18x20.DS18X20(onewire.OneWire(Pin(4)))

# cerca l'objecte definit i desa la seva adreça dins la variable roms, que té format de llista:
roms = ds_sensor.scan()                  
print('Trobat dispositiu DS: ', roms)    # mostra l'adreça trobada

while True:
    ds_sensor.convert_temp()  # llegeix el sensor i converteix les dades
    sleep (0.75)              # cal donar temps a realitzar l'acció anterior
    for rom in roms:          # per a cada element de la llista roms ...
        #print (rom)          # això mostra l'adreça del dispositiu ds_sensor
        #print (ds_sensor.read_temp(rom))             # mostra la temperatura
        print ('T=', ds_sensor.read_temp(rom), 'ºC')  # mostra la temperatura: magnitud, valor i unitat
    sleep (5)                 # interval d'actualització: 5 segons 
