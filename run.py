from flask import Flask, render_template, request, url_for
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)                #SETTING UP SERVO PINS AND PWM
GPIO.setwarnings(False)
p = GPIO.PWM(18, 50)
p.start(0)

@app.route("/")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('Google_SPEECH_API.html', **templateData)   #THIS SHOULD BE MAIN.HTML



@app.route("/<Num1>")
def readPin(Num1):
   new = int(Num1)
   p.ChangeDutyCycle(new)
   return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>WOLOLOLO</h1>
   </body>
</html>
'''
@app.route('/Decipher/', methods=['POST'])
def Decipher():
   Var1 = request.form['q']
   print (Var1)
   new1 = str(Var1)
   if (new1 == "right" or new1.startswith('ri') or new1.startswith('ry') or new1 == "bright"):
      p.ChangeDutyCycle(12)
   elif (new1 == "left" or new1.startswith('le') or new1.startswith('lo') or new1.startswith('li') or new1.startswith('ly') or new1 == "last"):
      p.ChangeDutyCycle(7)
   else:
      p.ChangeDutyCycle(0)
   return '''
<!DOCTYPE html>
   <head>
      <title>Redirect</title>
      <script language="javascript">
    window.location.href = "http://192.168.137.214:5000"
   </script>
   </head>

   <body>
   <h1>WOLOLOLO</h1>
   </body>
</html>
'''




if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True)