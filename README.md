# VoiceControlledServoMotor

This project is a simple way of controlling a servo motor connected to a raspberry pi through your VOICE wirelessly. The example also 
outlines a way of controlling the servo motor through the website so that someone could control it through a phone broswer as
well. This example opens up the user to edit and implement this to voice controlled robots, buggys, home automation with sound etc etc.

It uses a variety of existing online resources. I have just edited and compiled them for this easy tutorial. The languages in use
will be python, some html, some java script, some jquery and very limited css. It is recommended to be proficient in coding with python
and have some experience with making static and dynamic web pages through html.

System Description:

The total system consists of an HSR 1425CR servo motor connected to a raspberry pi. This raspberry pi is connected to the same wifi 
internet as the laptop on which you are developing the code. Through the web flask python framework, a web page will be hosted on the 
raspberry pi. Additionally Google web speech kit will be running on this webpage and whenever a trigger word is spoken it will automatically notify the raspberry pi and make it drive the motor.

Brief Description of Code:

Save run.py in your /home/pi directory. Install flask python framework and also read up on it. Flask is used inside run.py to host the first html page which will be accepting the inputs of voice from the user. The comments are self-explanatory.

Create a folder in your /home/pi called templates and save Google_SPEECH_api.html there. This html file has a lot of code and would take 
days to properly describe it. A brief explanation is attempted here. The code is a hybrid of google's developer web speech recognition code: https://developers.google.com/web/updates/2013/01/Voice-Driven-Web-Apps-Introduction-to-the-Web-Speech-API and "google voice triggered search code" http://www.labnol.org/software/add-speech-recognition-to-website/19989/ .
Basically the Google voice triggered search code instead of searching the spoken word on google sends it back to the raspberry pi who checks it and if it is right or left moves the motor accordingly. However this means the user must press the mic image every time he wants to communicate with the motor. Thus google's web speech kit is used to continuosly run on the computer and parse everything said by the user. Whenever it detects a trigger word it automatically triggers the above google voice search function which then detects what you say to the motor. After detecting what you say the page will be refreshed and the web speech kit will once again continue to record whatever you say. 

For ease of editing, current trigger word is 'kevin' after which you must say right or left to make motor move. To change the trigger word from kevin navigate to line 344 in Google_SPEECH_api.html and change kevin to whatevevr you want. To change motor words from left to right navigate to lines 26 and 28 in run.py and change them to whatever you want.
