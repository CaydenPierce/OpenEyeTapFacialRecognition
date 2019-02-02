import os.path
import numpy as np
from PIL import Image
import picamera
import picamera

'''
Converts numpy RGB array to image. Used when unknown face encoding is detected
'''

#create the camera, set to low resolution for faster processing
camera = picamera.PiCamera()
camera.resolution = (320, 240)

#array to store picture
image = np.empty((240, 320, 3), dtype=np.uint8)
camera.rotation = 90 # depends on the orientation of the pi camera

#start camera view
camera.start_preview()
camera.capture(image, format='rgb')


camera.stop_preview()

img = Image.fromarray(image, 'RGB')
img.save('gang.png')

