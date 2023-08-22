import socket    
import miwifi    
from machine import Pin, PWM

led = PWM(Pin(13), freq=5000) 

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servidor.bind(('', 80))
servidor.listen(5)

def pag_web():
    html="""<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Servidor PWM</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
<body>
<p>LLUMINOSITAT LED: <span id="textSliderValue">50</span> %</p>
<p><input type="range" onchange="updateSliderPWM(this)" id="pwmSlider" min="0" max="100" step="1" class="slider"></p>
<script>
function updateSliderPWM(element) {
  var sliderValue = document.getElementById("pwmSlider").value;
  document.getElementById("textSliderValue").innerHTML = sliderValue;
  console.log(sliderValue);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/slider?value="+sliderValue, true);
  xhr.send();
}
</script>
</body>
</html>"""
    return html

miwifi.connecta_wifi( )

while True:
    conn, addr = servidor.accept()
    print ('==========')
    print('Nova connexio des de', str(addr))
    request = conn.recv(1024)
    request = request.decode().split()    #split subdivideix una cadena en una llista. cal especificar els separadors

    if 'value' in request[1]:        # si la petició GET conté la paraula value
    # recordeu: l'ESP32 rebrà GET/slider?value=sliderValue
        valor_lliscador = request[1].split('&')[0].split('=')[1]
        # & i = son separadors del mètode split() per recuperar el valor de la petició GET
        print (valor_lliscador)  # valor rescatat del web (té format text). per comprovació
        valor_lliscador = int (valor_lliscador)    # transformo el resultat en text a nombre enter. Aquest sera el duty cap al led
        senyal_led = round (valor_lliscador*(1024/100))    # cal arrodonir el valor ?
        print (senyal_led)    # per comprovació
        led.duty (senyal_led)    # assignació del duty al pin del LED

    conn.send ('HTTP/1.1 200 OK\n')
    conn.send ('Content-Type: text/html\n')
    conn.send ('Connection: close\n\n')
    conn.sendall (pag_web())
    conn.close()
