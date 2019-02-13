# OpenEyeTap for Prosopagnosia 

In 2018, I became very interested in developing wearable technologies. I believe that the future of tech is on and within our bodies. This led me to build an OpenEyeTap smart eye glass, as I had found online after searching for opensource wearable. Not long after becoming interested in the OpenEyeTap hardware project, I met the incredible Dr. Steve Mann of MannLab, inventor of the EyeTap. He understood exactly the vision I put forward, and pointed me to his own research into the area of humanistic intelligence. Steve Mann proposed I build an EyeTap to function as a solution for individuals suffering from Prosopagnasia. I have done this. The program uses facial recognition to give a live display of the name of the individual that you are in conversation with.

INSTALL

OPTION 1
To try out the code on your EyeTap, you can simply flash the SD image onto your SD and plug and play in the OpenEyeTap.

OPTION 2
Clone this repo to hardware. Set .bashrc to start facerec_GUI.py upon booting by adding lines:

```
export DISPLAY=:0.0
python3 /home/pi/OpenEyeTapVirtualMemory/facerec_GUI.py
```
*replace path with your path.

This requires some GUI env already setup. I am using PIXEL and lightdm.

Follow https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65 to install face_recognition library. This library is simply a wrapper for the dlib library, which must also be installed and built.

Follow https://gist.github.com/kmpm/8e535a12a45a32f6d36cf26c7c6cef51 to setup GUI in Raspbian Stretch Lite.

Use raspi-config to enable picamera.

USE

The face file is an example of a face encoding. It is in CSV format and it loaded in python into a numpy array as such.

facerac.py utilizes the EyeTap principle but has an extrememly low framerate due to the extrememly week ARM core on the Pi Zero. Looking into solutions to this. NOTE: this supports bluetooth capability, with an Android app streaming NMEA to the pi. Will provide more info (and a bluetooth timeout) soon

facerec_GUI.py utilizes a simple tkinter GUI to display names of people recognized.

ADD NEW ENCODINGS

OPTION 1
Simply run NewFaceEncoder.py, which will take a picture and a name and then create a new encoding.

OPTION 2
Add .jpg's to /home/pi/newpeopleimages on the Pi. Name them the names of the people we want to encode i.e. CaydenPierce.jpg
Encodings will be created upon running the facerec scripts.



