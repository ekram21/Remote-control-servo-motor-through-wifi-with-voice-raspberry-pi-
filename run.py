from flask import Flask, render_template, request, url_for
import datetime
import RPi.GPIO as GPIO
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)                #SETTING UP SERVO PINS AND PWM
GPIO.setwarnings(False)
p = GPIO.PWM(18, 50)                   # This are all standard servo motor GPIO functions
p.start(0)

@app.route("/")                        # This will output the Google_SPEECH_API page to whoever goes to the addres http://localhost:5000  (replace localhost with the pi's IP address)
def hello():
   return render_template('Google_SPEECH_API.html')   



#This is what will happen after the webpage accepts what you say and sends it to the raspberry pi server .i.e here. The input is converted to a string and then based on what it is used to decide direction of motor
@app.route('/Decipher/', methods=['POST'])
def Decipher():
   Var1 = request.form['q']
   print (Var1)
   new1 = str(Var1)
   if (new1 == "right" or new1.startswith('ri') or new1.startswith('ry') or new1 == "bright"):   #If spoken word is right/bright or starts with ri/ry make motor turn one way
      p.ChangeDutyCycle(12)
   elif (new1 == "left" or new1.startswith('le') or new1.startswith('lo') or new1.startswith('li') or new1.startswith('ly') or new1 == "last"): #same as above only in opposite direction
      p.ChangeDutyCycle(7)
   else:
      p.ChangeDutyCycle(0)
      #The below will be returned to the user on the webpage. Since we want it to redirect back to Google_speech_API the window.location.href will redirect it. Change the ip addres before :5000 to your pi's ip address
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




if __name__ == "__main__":             #This runs the program and hosts the webpage
   app.run(host='0.0.0.0', debug=True)
