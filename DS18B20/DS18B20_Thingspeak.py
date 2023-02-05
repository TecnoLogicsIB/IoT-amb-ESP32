""" Llegeix la temperatura de dos sensors DS18B20 i puja les dades a Thingspeak """

# importa mòduls:
import onewire, ds18x20    # per interactuar amb el sensor DS18B20
from machine import Pin    # per interactuar amb els GPIO
from time import sleep     # per definir pauses

import urequests           # per fer peticions HTTP al servidor de Thingspeak
import miwifi              # llibreria que conté la funció per connectar a WiFi

# url d'actualització de dades al meu canal de Thingspeak:
url = 'https://api.thingspeak.com/update?api_key=BK5LJ7G6KJN1FD3A'
# executa la funció de connexió a wiFi:
miwifi.connecta_wifi()

# creació d'objecte ds18x20 associat al pin de connexió del sensor:
sensor = ds18x20.DS18X20(onewire.OneWire(Pin(4)))
# cerca l'objecte definit i desa la seva adreça dins la variable adreces, que té format de llista:
adreces = sensor.scan()                  
print('Trobat dispositiu DS: ', adreces)    # mostra l'adreça trobada

while True:
    sensor.convert_temp()     # llegeix el sensor i converteix les dades
    sleep (0.75)              # cal donar temps a realitzar l'acció anterior
    # variable per desar la temperatura llegida per cada sensor:
    Tint = sensor.read_temp(adreces[0])
    Text = sensor.read_temp(adreces[1])
    
    # envia les dades al meu canal de Thingspeak:
    peticio = urequests.get(url+ '&field1=' + str(Tint) + '&field2=' + str(Text))
    print (peticio.text, peticio.status_code)
    peticio.close ()
    
    # mostra les temperatures (per comprobació):
    print ('Tint=', Tint, 'ºC')    
    print ('Text=', Text, 'ºC')
    print ('=================')
    sleep (15)                 # interval d'actualització de Thingspèak: 15 segons
    
