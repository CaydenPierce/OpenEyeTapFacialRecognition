import face_recognition
import os
import numpy as np
import picamera
from time import sleep
import csv
import datetime


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

def getEncoding(imageURI):

    #load image from file
    unknownFace = face_recognition.load_image_file(imageURI)

    #create encoding
    uknownFaceEncoding = face_recognition.face_encodings(unknownFace)
    return uknownFaceEncoding


def loadNewPeople():
    #first, load list of names of new people
    names = []
    files = []
    
    for file in os.listdir("./newpeopleimages"):
        if not (file.startswith("ToName")): #this is used as all pictures that requiring labelling are appended with the suffix "ToName"-, followed by the time the picture was taken
            files.append(file)
            a = file.partition(".")[0] #remove file extension
            for i, char in enumerate(a[1:]):
                if char.isupper():
                    firstName = a[:i+1]
                    lastName = a[i+1:]
            names.append([firstName, lastName])

    for i, file in enumerate(files):
        fullName = names[i][0] + " " + names[i][1]
        saveEncoding((getEncoding("./newpeopleimages/{}".format(file))), fullName)
        print(getEncoding("./newpeopleimages/{}".format(file)))
        print(file)
        os.system("cp {} {}".format(("./newpeopleimages/{}".format(file)), ("./knownpeopleimages/{}".format(file))))
        #os.remove("./newpeopleimages/{}".format(file))
            
def loadKnownEncodings():
    knownEncodings = []
    names = []
    peopleDB = {} #this dict holds the names of people and their related face encodings
    for i, file in enumerate(os.listdir("./encodings")):
        currentEncoding = openEncoding("./encodings/{}".format(file))
        knownEncodings.append(currentEncoding)
        a = file.partition(".")[0] #remove file extension
        for j, char in enumerate(a[1:]):
            if char.isupper():
                firstName = a[:j+1]
                lastName = a[j+1:]
        names.append([firstName, lastName])
        peopleDB[(names[i][0] + " " + names[i][1])] = currentEncoding; # Add new entry
    knownEncodings = np.array(knownEncodings)       
    return knownEncodings, peopleDB
        

#first, load any new people we want to add to our database of encodings
loadNewPeople()

#now load all encodings we have in the database
#knownEncodings, peopleDB = loadKnownEncodings() #this is the people database

#print(knownEncodings)
#print(peopleDB)
