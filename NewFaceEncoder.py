import face_recognition
import numpy as np
import picamera

def getEncoding(imageURI):

    #load image from file
    unknownFace = face_recognition.load_image_file(imageURI)

    #create encoding
    print("Processing...")
    uknownFaceEncoding = face_recognition.face_encodings(unknownFace)
    print("Created!")
    return uknownFaceEncoding

