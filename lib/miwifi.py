import network                    # la llibreria network permet connectar en xarxa
from time import sleep            # importa la classe sleep de la llibreria time

# dades xarxa WiFi
ssid = 'vodafoneE3D9'              # nom de la xarxa
psw = 'JU7AJW8YFWMWLR'             # contrassenya

def connecta_WiFi():
    estacio = network.WLAN (network.STA_IF)     # configuració del dispositiu com a estació WiFi (amb el nom que volguem)
    estacio.active (False)         # desactivació prèvia per si d'acàs
    estacio.active (True)          # activa el mode estació
    estacio.connect(ssid, psw)     # connecta a la xarxa definida
    print ("Conectant a WiFi")     # mostra missatge a la consola
    while not estacio.isconnected():      # mentre no estigui connectat, l'execució es mantindrà en aquest bucle:
        print (".", end="")               # barra de progrés (end="") fa que s'imprimeixi tot en la mateixa línia       
        sleep (0.1)
    print ("Connectat a", ssid)    # un cop connectat, surt del bucle anterior i mostra missatge de confirmació
    # print(estacio.ifconfig())    # retorna totes les dades de la connexió (adreça IP, màscara de xarxa, gateway, i DNS)
    print("connecta't al servidor: ", estacio.ifconfig()[0])     # retorna l'adreça IP de l'ESP32. Suficient per a servidor web