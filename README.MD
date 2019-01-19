VIRTUAL MEMORY

Raymond Kurzweil, the leading innovator, thinker, futurist, and author claims in his last two books (The Singularity is Near and How to Create a Mind) that the future of technology lies in an ever increasing symbiosis between biological intelligence and artificial intelligence. I agree with this vision, and realize that the businesses of the future will be those that take into account the ever growing intimacy that we experience with our machines.

Not long after becoming interested in this project, I met the incredible inventor Dr. Steve Mann of MannLab. He understood exactly the vision I put forward, and pointed me to his own research into this very device, dating back over 20 years.

This is the aim of my virtual memory product. I am developing a system that, when attached to a user (either around the neck of in a headset) records video and audio input. The differing sources of information comes together to become what I refer to as “virtual memories’. The information is then connected to other virtual “memories” by analyzing patterns that new information shares with old information. In essence, this technology will align sensory input into a coherent structure, just as our biological memory works, except with perfect recall. This is being paired with multiple technologies, such as face and image recognition, to provide the “scenarios” and connections that is used by the software when making connections between memories.

INSTALL

OPTION 1
To try out the code on your EyeTap, you can simply flash the SD image onto your SD and plug and play in the OpenEyeTap.

OPTION 2
Clone this repo to hardware. Set .bashrc to start facerec_GUI.py upon booting. This requires some GUI env already setup. I am using PIXEL and lightdm.

Follow https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65 to install face_recognition library. This library is simply a wrapper for the dlib library, which must also be installed and built.

Follow https://gist.github.com/kmpm/8e535a12a45a32f6d36cf26c7c6cef51 to setup GUI in Raspbian Stretch Lite.

Use raspi-config to enable picamera.

USE

The face file is an example of a face encoding. It is in CSV format and it loaded in python into a numpy array as such.

facerac.py utilizes the EyeTap principle but has an extrememly low framerate due to the extrememly week ARM core on the Pi Zero. Looking into solutions to this.

facerec_GUI.py utilizes a simple tkinter GUI to display names of people recognized.

ADD NEW ENCODINGS

OPTION 1
Simply run NewFaceEncoder.py, which will take a picture and a name and then create a new encoding.

OPTION 2
Add .jpg's to /home/pi/newpeopleimages on the Pi. Name them the names of the people we want to encode i.e. CaydenPierce.jpg
Encodings will be created upon running the facerec scripts.



