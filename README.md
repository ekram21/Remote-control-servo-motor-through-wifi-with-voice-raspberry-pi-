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
raspberry pi. This webpage will allow any user to directly control the motor using buttons/links. Additionally Google web speech kit will
be running on this webpage and whenever a trigger word is spoken it will automatically notify the raspberry pi and make it drive the motor.
