'''
Wearable Face Recognizer for the OpenEyeTap
Created by Cayden Pierce. Some code borrowed from dashcam utility created by the OpenEyeTap team.
This can be used by everyone.
An especially interesting application for sufferers of prosopagnosia.
Humanistic Intelligence is the future we are all creating together.
'''


import face_recognition
import os
import numpy as np
import picamera
from time import sleep
import csv
import datetime
from time import sleep
import datetime as dt
from blue import GPSbluetooth
import json
from PIL import Image
import requests


#this program controls the face recognition abilities of the OpenEyeTap
#First, any images that have been added to the 'newpeople' folder are loaded, and an encoding is made based on each face. The encoding and the name of the individual is then saved in the encodings folder,
#and the picture is deleted from the 'newimages' folder
#the program then begins watching the camera, if a person is detected, their name is displayed. If the person is not recognized, a picture of the individual is then saved in the 'newpeople' folder for later labelling by the user

#open encoding CSV and create list
def openEncoding(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        encoding = list(reader)
        encoding = np.array(encoding[0])
    encoding = encoding.astype(np.float)
    return encoding

#saves encoding to CSV file
def saveEncoding(encoding, fileName, which): #pass the encodign, what we want to name it, and whether it is a knonw person or unknown person (who needs to be named by user)
    if fileName:
        imageFileName = fileName
    else:
        #create name of file using current date and time
        imageFileName = "unkownFaceDataTakenAt_{}_{}".format(datetime.datetime.now().date(), datetime.datetime.time(datetime.datetime.now()))
    #save encoding to csv
    with open(("./{}_encodings/{}".format(which, imageFileName)), "w", newline="") as myEncodingFile:
        wr = csv.writer(myEncodingFile, delimiter = ',')
        wr.writerows(encoding)

#create encoding  given URI
def getEncodingURI(imageURI):
    #load image from file
    unknownFace = face_recognition.load_image_file(imageURI)

    #create encoding
    print("Processing...")
    uknownFaceEncoding = face_recognition.face_encodings(unknownFace)
    print("Created new encoding for {}!".format(imageURI))
    return uknownFaceEncoding

#get encoding given an image
def getEncodingImg(image):    

    #create encoding
    unknownFaceEncoding = face_recognition.face_encodings(image)
    return unknownFaceEncoding


def loadNewPeople():
    #first, load list of names of new people
    names = []
    files = []
    
    for file in os.listdir("./newpeopleimages"):
        files.append(file)
        if not (file.startswith("ToName")): #this is used as all pictures that requiring labelling are appended with the suffix "ToName"-, followed by the time the picture was taken
            a = file.partition(".")[0] #remove file extension
            for i, char in enumerate(a[1:]):
                if char.isupper():
                    firstName = a[:i+1]
                    lastName = a[i+1:]
                    names.append([firstName, lastName])
                    break
    
    for i, file in enumerate(files):
        if not (file.startswith("ToName")): #this is used as all pictures that requiring labelling are appended with the suffix "ToName"-, followed by the time the picture was taken
            fullName = names[i][0] + " " + names[i][1]
            #load image from file
            print("./newpeopleimages/{}".format(file))
            saveEncoding(getEncodingURI("./newpeopleimages/{}".format(file)), fullName, 'known')
            os.system("cp {} {}".format(("./newpeopleimages/{}".format(file)), ("./knownpeopleimages/{}".format(file))))
            os.remove("./newpeopleimages/{}".format(file))
            
def loadKnownEncodings(): #loads known encodings
    knownEncodings = []
    names = []
    peopleDB = [] #this holds the names 
    for i, file in enumerate(os.listdir("./known_encodings")):
        currentEncoding = openEncoding("./known_encodings/{}".format(file))
        #print(currentEncoding)
        knownEncodings.append(currentEncoding)
        a = file.partition(".")[0] #remove file extension
        for j, char in enumerate(a[1:]):
            if char.isupper():
                firstName = a[:j+1]
                lastName = a[j+1:]
        names.append([firstName, lastName])
    knownEncodings = np.array(knownEncodings)       
    return knownEncodings, names

def loadUnknownEncodings(): #loads unknown encodings
    unknownEncodings = []
    for i, file in enumerate(os.listdir("./unknown_encodings")):
        currentEncoding = openEncoding("./unknown_encodings/{}".format(file))
        unknownEncodings.append(currentEncoding)
        a = file.partition(".")[0] #remove file extension
    unknownEncodings = unknownEncodings  
    return unknownEncodings

def CurrentTime():
    return('%s')%(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def sec():
    sec.var = dt.datetime.now().strftime('%S')
    return sec.var

sec.var=0 # initializes the sec variable, to be used later

def Timestamp():
    # Adds a timestamp to each frame
    if (dt.datetime.now().strftime('%S') != sec.var): # accesses the second value from the last time sec() was called
        # updates the annotation on the video if a second has passed
        camera.annotate_text_size = 60
        camera.annotate_background = picamera.Color('black')
        camera.annotate_text = CurrentTime()
        sec() # calls the second function so that it can update its current second value

def getAddress(lat, long):
    try:
        url = "https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1".format(str(lat), str(long))
        response = requests.get(url)
        data= response.json()
        house_number = data['address']['house_number']
        road = data['address']['road']
        city = data['address']['city']
        return data['display_name']
    except Exception:
        return ("Latitude: " + lat + " Longitude: " + long)

def createLog(name): #adds log of seeing person. Contains context such as who, what, where, when
        time = CurrentTime()
        lat, long = GPSbluetooth.getLocation(sock)
        location = getAddress(lat, long)
        memory = [time, location, name]
        #check if last log was same person before writing (don't write if same person within 5 minutes()
        if not ((prevMemory[0] == memory[2]) and (dt.datetime.now()-prevMemory[1]).total_seconds < 300):
            with open("./memory/lifelog.csv", "a", newline="") as log_csv: #open in append and read mode
                wr = csv.writer(log_csv, delimiter = ',')
                wr.writerow(memory)
        prevMemory = [name, dt.datetime.now()]   
        
#start the bluetooth server for GPS, save socket
sock = GPSbluetooth.startBluetoothServer()

#first, load any new people we want to add to our database of encodings
loadNewPeople()

#then, load all the poeple we already know, and all the people we haven't yet named
knownEncodings, names = loadKnownEncodings()
unknownEncodings = loadUnknownEncodings()

#create the camera, set to low resolution for faster processing
camera = picamera.PiCamera()
camera.resolution = (320, 240)

#array to store picture
image = np.empty((240, 320, 3), dtype=np.uint8)
camera.rotation = 90 # depends on the orientation of the pi camera

#start camera view
camera.start_preview()

#counter for testing
counter = 0

while counter < 15:
#main program loop
    counter += 1
    print("loop {}".format(counter))

    # Shows timestamp on top of video
    #Timestamp() 
    
    #take pic
    camera.capture(image, format='rgb')


    #scan for faces
    face_locations = face_recognition.face_locations(image)
    
    if face_locations: #runs if face is detected
        #create encoding
        unknownFaceEncoding = getEncodingImg(image)
        faceMatchList = face_recognition.compare_faces(knownEncodings, unknownFaceEncoding)
        #print(faceMatchList)
        for i, value in enumerate(faceMatchList):
            if value:
                fullName = names[i][0] + names[i][1]
                camera.annotate_text = fullName
                print("I see {}!".format(fullName))
                #v.set(fullName)
                createLog(fullName)
                break
            else:
                fullName = "Unknown person"
        camera.annotate_text = fullName
        #v.set(fullName)
        if (fullName == "Unknown person"): #saves pictures and encodings of unknown people to be later named
            #create encoding
            unknownFaceEncoding = getEncodingImg(image)
            unknownFaceEncoding_append = (np.array(unknownFaceEncoding[0])).astype(np.float) #processing so it can be passed to face_recognition
            print(unknownFaceEncoding)
            print(unknownFaceEncoding_append)
            faceMatchList = face_recognition.compare_faces(np.array(unknownEncodings), unknownFaceEncoding)
            if not np.any(faceMatchList): #if none are true, then we save image and encoding
                unknownEncodings.append(unknownFaceEncoding_append) #add it to our list of unknown encodings, stops us from resaving images of same person
                #print(unknownEncodings)
                time = CurrentTime()
                img = Image.fromarray(image, 'RGB')
                img.save('./newpeopleimages/ToName{}.jpg'.format(time))
                saveEncoding(unknownFaceEncoding, 'ToName{}'.format(time), 'unknown')     
    else:
        #reset annotation
        camera.annotate_text = ""
sock.close()      
camera.stop_preview()
