import picamera
from time import sleep


camera = picamera.PiCamera()
camera.resolution = (320, 240)
image = "./images/test_image.jpg"

camera.start_preview()
# Camera warm-up time
sleep(2)

camera.capture("./images/test_image.jpg", format='jpeg')
camera.stop_preview()
