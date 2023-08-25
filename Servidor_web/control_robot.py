import socket    
import miwifi    
from machine import Pin, PWM

servo1 = PWM(Pin(19),freq=50)
servo2 = PWM(Pin(18),freq=50)
servo3 = PWM(Pin(5),freq=50)
servo4 = PWM(Pin(17),freq=50)
servo5 = PWM(Pin(16),freq=50)

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
servidor.bind(('', 80))
servidor.listen(5)

def pag_web():
    html="""<html>
<head>
<title>ESP32 Servidor Web</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
</head>
<body>
<p>POSICIO SERVO 1: <span id="textSliderValue1">50</span></p>
<p><input type="range" onchange="updateSliderPWM1(this)" id="pwmSlider1" max="180" min="0" step="1" class="slider"></p>
<p>POSICIO SERVO 2: <span id="textSliderValue2">50</span></p>
<p><input type="range" onchange="updateSliderPWM2(this)" id="pwmSlider2" min="0" max="180" step="1" class="slider"></p>
<p>POSICIO SERVO 3: <span id="textSliderValue3">50</span></p>
<p><input type="range" onchange="updateSliderPWM3(this)" id="pwmSlider3" min="0" max="180" step="1" class="slider"></p>
<p>POSICIO SERVO 4: <span id="textSliderValue4">50</span></p>
<p><input type="range" onchange="updateSliderPWM4(this)" id="pwmSlider4" min="0" max="180" step="1" class="slider"></p>
<p>POSICIO SERVO 5: <span id="textSliderValue5">50</span></p>
<p><input type="range" onchange="updateSliderPWM5(this)" id="pwmSlider5" min="0" max="180" step="5" class="slider"></p>
<script>
function updateSliderPWM1(element) {
  var sliderValue1 = document.getElementById("pwmSlider1").value;
  document.getElementById("textSliderValue1").innerHTML = sliderValue1;
  console.log(sliderValue1);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/slider1?value="+sliderValue1, true);
  xhr.send();
}
function updateSliderPWM2(element) {
  var sliderValue2 = document.getElementById("pwmSlider2").value;
  document.getElementById("textSliderValue2").innerHTML = sliderValue2;
  console.log(sliderValue2);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/slider2?value="+sliderValue2, true);
  xhr.send();
}
function updateSliderPWM3(element) {
  var sliderValue3 = document.getElementById("pwmSlider3").value;
  document.getElementById("textSliderValue3").innerHTML = sliderValue3;
  console.log(sliderValue3);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/slider3?value="+sliderValue3, true);
  xhr.send();
}
function updateSliderPWM4(element) {
  var sliderValue4 = document.getElementById("pwmSlider4").value;
  document.getElementById("textSliderValue4").innerHTML = sliderValue4;
  console.log(sliderValue4);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/slider4?value="+sliderValue4, true);
  xhr.send();
}
function updateSliderPWM5(element) {
  var sliderValue5 = document.getElementById("pwmSlider5").value;
  document.getElementById("textSliderValue5").innerHTML = sliderValue5;
  console.log(sliderValue5);
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "/slider5?value="+sliderValue5, true);
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

    if 'slider1' in request[1]:        
        valor_lliscador1 = request[1].split('&')[0].split('=')[1]
        print (valor_lliscador1)  
        valor_lliscador1 = int (valor_lliscador1)    
        senyal_servo1 = round (valor_lliscador1*(100/180)+25)
        print (senyal_servo1)
        servo1.duty(senyal_servo1)
    if 'slider2' in request[1]:        
        valor_lliscador2 = request[1].split('&')[0].split('=')[1]
        print (valor_lliscador2)  
        valor_lliscador2 = int (valor_lliscador2)    
        senyal_servo2 = round (valor_lliscador2*(100/180)+25)
        print (senyal_servo2)
        servo2.duty(senyal_servo2)
    if 'slider3' in request[1]:        
        valor_lliscador3 = request[1].split('&')[0].split('=')[1]
        print (valor_lliscador3)  
        valor_lliscador3 = int (valor_lliscador3)    
        senyal_servo3 = round (valor_lliscador3*(100/180)+25)
        print (senyal_servo3)
        servo3.duty(senyal_servo3)
    if 'slider4' in request[1]:        
        valor_lliscador4 = request[1].split('&')[0].split('=')[1]
        print (valor_lliscador4)  
        valor_lliscador4 = int (valor_lliscador4)    
        senyal_servo4 = round (valor_lliscador4*(100/180)+25)
        print (senyal_servo4)
        servo4.duty(senyal_servo4)
    if 'slider5' in request[1]:        
        valor_lliscador5 = request[1].split('&')[0].split('=')[1]
        print (valor_lliscador5)  
        valor_lliscador5 = int (valor_lliscador5)    
        senyal_servo5 = round (valor_lliscador5*(100/180)+25)
        print (senyal_servo5)
        servo5.duty(senyal_servo5)

    conn.send ('HTTP/1.1 200 OK\n')
    conn.send ('Content-Type: text/html\n')
    conn.send ('Connection: close\n\n')
    conn.sendall (pag_web())
    conn.close()
