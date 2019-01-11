import face_recognition
import numpy as np
import picamera
from time import sleep

#create encoding for given image
def getEncoding(imageURI):
    #load image from file
    unknownFace = face_recognition.load_image_file(imageURI)

    #create encoding
    print("Processing...")
    uknownFaceEncoding = face_recognition.face_encodings(unknownFace)
    print("Created!")
    return uknownFaceEncoding

#saves encoding to CSV file
def saveEncoding(encoding, fileName):
    if fileName:
        imageFileName = fileName
    else:
        #create name of file using current date and time
        imageFileName = "unkownFaceDataTakenAt_{}_{}".format(datetime.datetime.now().date(), datetime.datetime.time(datetime.datetime.now()))
    #save encoding to csv
    with open(("./encodings/{}".format(imageFileName)), "w", newline="") as myEncodingFile:
        wr = csv.writer(myEncodingFile, delimiter = ',')
        wr.writerows(encoding)

personName = input("What is the name?")

camera = picamera.PiCamera()

camera.start_preview()
camera.annotate_text = "Say CHEESE!"
sleep(5)
camera.capture("./new.jpg")
camera.stop_preview()

myEncoding = getEncoding("./new.jpg")

saveEncoding(myEncoding, personName)




