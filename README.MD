TECHNICAL

To try out the code on your EyeTap, upload facerec.py to hardware. Set .bashrc to start tester.py upon booting. This requires some GUI env already setup. I am using PIXEL and lightdm.

Follow https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65 to install face_recognitino library.

Follow https://gist.github.com/kmpm/8e535a12a45a32f6d36cf26c7c6cef51 to setup GUI in Raspbian Stretch Lite.

Use raspi-config to enable picamera.

The face file is an example of a face encoding. It is in CSV format and it loaded in python into a numpy array as such.

MAIN is the current work file. I am developing the software directly on a Pi 3B+ to speed up development time by avoiding having to upload to the Pi Zero too often. This can be run on any Pi with a PiCamera.

VIRTUAL MEMORY

Raymond Kurzweil, the leading innovator, thinker, futurist, and author claims in his last two books (The Singularity is Near and How to Create a Mind) that the future of technology lies in an ever increasing symbiosis between biological intelligence and artificial intelligence. I agree with this vision, and realize that the businesses of the future will be those that take into account the ever growing intimacy that we experience with our machines.

This is the aim of my virtual memory product. I am developing a system that, when attached to a user (either around the neck of in a headset) records video and audio input. The differing sources of information comes together to become what I refer to as “virtual memories’. The information is then connected to other virtual “memories” by analyzing patterns that new information shares with old information. In essence, this technology will align sensory input into a coherent structure, just as our biological memory works, except with perfect recall. This is being paired with multiple technologies, such as face and image recognition, to provide the “scenarios” and connections that is used by the software when making connections between memories.


