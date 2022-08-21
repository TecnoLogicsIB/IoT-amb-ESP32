""" servidor que mostra informació en una pàgina web """

# importa llibreries:
import socket      # permet crear i gestionar servidors web
import miwifi      # definició de la connexió a wiFi, desada al dispositiu com a llibreria

# configuració del servidor:
servidor = socket.socket (socket.AF_INET, socket.SOCK_STREAM)    # objecte socket que he anomenat servidor  
# el mètode .bind enllaça el sòcol amb una adreça IP i un port (80 és el port per defecte):
servidor.bind(('', 80))   # l'argument '' com a adreça IP fa referència a l'adreça IP de l'host local (l' ESP32) 
servidor.listen(5)        # el mètode listen() permet que el servidor accepti el núm de connexions definit (màx 5)

# la resposta del servidor serà en format pàgina web:
def pag_web():
    # la variable que he anomenat html conté la definició de la pàgina web en format HTML:
    html = """<html>
              <head> <title>Servidor Web Demo</title>
              <meta name="viewport" content="width=device-width, initial-scale=1.0"> </head>
              <body> <p>Mi Servidor</p>
              <p>Hola, """ + str(addr)+ """</p>
              <p>Servidor web en marxa!</p>
              </body>
              </html>"""
    return html     # per poder utilitzar la variable fora de la funció en que està definida

# executa la connexió a WiFi, definida a l'arxiu miwifi.py:
miwifi.connecta_WiFi() 

# En el bucle while True és on escoltem les sol·licituds i enviem respostes:
while True:
    conn, addr = servidor.accept()                 # quan un client es connecti, accepta la connexió
    # conn: nou objecte de sòcol per acceptar i enviar dades 
    # addr: variable on es desa l'adreça del client que es vol connectar al servidor
    addr = str(addr)                               # cal convertir el format a cadena de caracters (string)
    print ('Nova connexió des de', str(addr))      # imprimeix l'adreça del client, desada en la variable addr

    peticio = conn.recv(1024)      # desa la sol·licitud rebuda al sòcol en la variable peticio 
    # l'argument de recv(1024) especifica el màxim de dades que es poden rebre alhora
    print (str (peticio))          # imprimeix el contingut de la sol·licitud. str converteix a string
    print ('==========')           # separador per llegir millor a la consola
      
    # envia la resposta al client mitjançant els mètodes send() i .sendall():
    conn.send ('HTTP/1.1 200 OK\n')
    conn.send ('Content-Type: text/html\n')
    conn.send ('Connection: close\n\n')
    conn.sendall (pag_web())       # envia com a resposta el text HTML retornat per la funció pag_weg  
    conn.close()                   # tanca el sòcol creat
