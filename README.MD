# Wearable Face Recognizer

I am very interested in developing wearable technologies. I believe that the future of tech is on and within our bodies. This led me to build an OpenEyeTap smart eye glass, as I had found online after searching for opensource wearables. Not long after becoming interested in the OpenEyeTap hardware project, I met Dr. Steve Mann of MannLab, inventor of the EyeTap. He understood exactly the vision I put forward, and pointed me to his own research into the area of Humanistic Intelligence systems. Steve Mann proposed I build an EyeTap to function as a solution for individuals suffering from prosopagnasia. I have done this. The program uses facial recognition to give a live display of the name of the individual that you are in conversation with.

## INSTALL

### OPTION 1
*NOTE: This is an older version
To try out the code on your EyeTap, you can simply flash the SD image onto your SD and plug and play in the OpenEyeTap. (You will need a => 32GB card... will make a smaller one soon. If you want it smaller, mount it and configure using dd bash tool.)

Image: https://drive.google.com/file/d/1ZZagIRXM0wIGF5QBK9OQ5Fzi3HPLsdFC/view?usp=sharing

### OPTION 2

Clone this repo to hardware. Set .bashrc to start FaceRecognizer.py upon booting by adding lines:

```
export DISPLAY=:0.0
python3 /home/pi/OpenEyeTapVirtualMemory/FaceRecognizer.py
```
*replace path with your path.

This requires some GUI env already setup. I am using PIXEL and lightdm:

Follow https://gist.github.com/kmpm/8e535a12a45a32f6d36cf26c7c6cef51 to setup GUI in Raspbian Stretch Lite.

Face recognition is based on the highly accurate dlib C++ face_recognition model:

Follow https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65 to install face_recognition library. This library is simply a wrapper for the dlib library, which must also be installed and built.

Follow instructions in DISABLESCREENSAVER.MD to disable screensaver in PIXEL.

Install dependencies (for Python3):

```

sudo apt-get install python3-tk
pip install numpy pybluez pynmea2

```
*there may be more, just follow the prompts if errors occur. I need to setup a proper python virtualenv for this reason.
 
Use raspi-config to enable picamera in Raspbian.

## USE

### FaceRecognizer.py

This utilizes a GUI to display names of people recognized. Memories are stored every time you see a new person. Name, time, and location data is saved in a lifelog file in ./memory

### FaceRecognizer_noBluetooth.py

No bluetooth on this one, in case you don't have an Android with the GPS app working. This utilizes a GUI to display names of people recognized. Memories are stored every time you see a new person. Name, time data is saved in a lifelog file in ./memory.

### facerec.py

This utilizes the EyeTap principle but has an extrememly low framerate due to the extrememly week ARM core on the Pi Zero. Looking into solutions to this. NOTE: this supports bluetooth capability, with an Android app streaming NMEA to the pi. Will provide more info (and a bluetooth timeout) soon

### Other

The face file is an example of a face encoding. It is in CSV format and it loaded in python into a numpy array as such.

FaceRecognizer.py utilizes a GUI to display names of people recognized. This supports memories and GPS.

## HOW TO ADD NEW PEOPLE

### Option 1
Simply run NewFaceEncoder.py, which will take a picture and a name and then create a new encoding.

### Option 2
Add .jpg's to /home/pi/newpeopleimages on the Pi. Name them the names of the people we want to encode in FirstnameLastname.jpg style. i.e. CaydenPierce.jpg. Encodings will be created upon running the facerec scripts.

### Option 3

Simply wear the device around. Everyone you see that isn't recognized will be added to the ./newpeopleimages/ folder, where you can then log in and name them easily.

## GPS setup

Turn on Bluetooth on pi, make discoverable, trust your phone, then:

Run "Share GPS" app on your Anroid phone.:

http://www.jillybunch.com/sharegps/

And pair your phone to your pi. Make your device visible in the "Share GPS" app.

Your phone will now stream NMEA data to the OpenEyeTap. Latitiude and Longitude is converted into addresses, destinations, and institutions. 

# Soon to come

Audio/Voice support, Speedometer, Virtual Memory, Full database support - done, Emotion recognition, Lifelogging (Glogging)


# Help

Please reach out if you need a hand, have any problems, want to add something, or just want to talk wearables and HI!

Email: cpierc3 at uwo dottt  ca 
