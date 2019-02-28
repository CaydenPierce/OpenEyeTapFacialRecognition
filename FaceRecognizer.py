'''
Wearable Face Recognizer for the OpenEyeTap
Created by Cayden Pierce. Some code borrowed from dashcam utility created by the OpenEyeTap team.
This can be used by everyone.
An especially interesting application for sufferers of prosopagnosia.
Humanistic Intelligence is the future we are all creating together..
'''


from blue import GPSbluetooth
import face_recognition
import os
import numpy as np
import picamera
import csv
from time import sleep
import datetime as dt
import tkinter as tk
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
def saveEncoding(encoding, fileName):
    if fileName:
        imageFileName = fileName
    else:
        #create name of file using current date and time
        imageFileName = "unkownFaceDataTakenAt_{}_{}".format(datetime.datetime.now().date(), datetime.datetime.time(datetime.datetime.now()))
    #save encoding to csv
    with open((os.path.join(os.path.dirname(__file__), "known_encodings/{}".format(imageFileName))), "w", newline="") as myEncodingFile:
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
    
    for file in os.listdir(os.path.join(os.path.dirname(__file__), "newpeopleimages")):
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
        fullName = names[i][0] + " " + names[i][1]
        #load image from file
        #print("./newpeopleimages/{}".format(file))
        saveEncoding(getEncodingURI((os.path.join(os.path.dirname(__file__), "newpeopleimages/{}".format(file))), fullName))
        os.system("cp {} {}".format(("./newpeopleimages/{}".format(file)), ("./knownpeopleimages/{}".format(file))))
        os.remove(os.path.join(os.path.dirname(__file__), "newpeopleimages/{}".format(file)))
            
def loadEncodings(which): #loads known or unknown encodings
    knownEncodings = []
    names = []
    peopleDB = [] #this holds the names 
    for i, file in enumerate(os.listdir(os.path.join(os.path.dirname(__file__), "{}_encodings".format(which)))):
        currentEncoding = openEncoding(os.path.join(os.path.dirname(__file__), "{}_encodings/{}".format(which, file)))
        knownEncodings.append(currentEncoding)
        a = file.partition(".")[0] #remove file extension
        for j, char in enumerate(a[1:]):
            if char.isupper():
                firstName = a[:j+1]
                lastName = a[j+1:]
        names.append([firstName, lastName])
    knownEncodings = np.array(knownEncodings)       
    return knownEncodings, names

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
    #try:
        url = "https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1".format(str(lat), str(long))
        response = requests.get(url)
        data= response.json()
        house_number = data['address']['house_number']
        road = data['address']['road']
        city = data['address']['city']
        return data['display_name']
   # except Exception:
        #return ("Latitude: " + str(lat) + " Longitude: " + str(long))

def createLog(name): #adds log of seeing person. Contains context such as who, what, where, when
        with open(os.path.join(os.path.dirname(__file__), "memory/lifelog.csv"), "a", newline="") as log_csv: #open in append and read mode
            time = CurrentTime()
            coordinates = GPSbluetooth.getLocation(sock)
            if coordinates:
            	lat, long = coordinates
            	location = getAddress(lat, long)
            else:
            	location = ("Latitude: {}, Longitude: {}".format(lat, long))
            memory = [time, location, name]

            wr = csv.writer(log_csv, delimiter = ',')
            wr.writerow(memory)
            
        
#start the bluetooth server for GPS, save socket
sock = GPSbluetooth.startBluetoothServer()

#first, load any new people we want to add to our database of encodings
loadNewPeople()

#then, load all the poeple we already know
knownEncodings, names = loadEncodings("known")

#create the camera, set to low resolution for faster processing
camera = picamera.PiCamera()
camera.resolution = (320, 240)
camera.rotation = 90
#array to store picture
image = np.empty((240, 320, 3), dtype=np.uint8)

#start camera view
#camera.start_preview()


#Following is the GUI window, creating a label and setting attributes
root = tk.Tk()
root.configure(background='black')
root.attributes('-zoomed', True) #setting dispaly fullscreen
root.attributes('-fullscreen',True)
root.config(cursor="none") #disable cursor
#root.attributes("-fullscreen", True)  # substitute `Tk` for whatever your `Tk()` object is called
v = tk.StringVar()
w = tk.Label(root, textvariable=v, font=(None, 65), bg = 'black', fg = 'white', wraplength=600, justify="center")
w.config(bg="black")
w.pack()

while True: #main program loop

    # Shows timestamp on top of video - optional
    #Timestamp()    
    #take pic
    camera.capture(image, format='rgb')


    #scan for faces
    face_locations = face_recognition.face_locations(image)

    #runs if face is detected
    if face_locations:
        #create encoding
        unknownFaceEncoding = getEncodingImg(image)
        #check for match
        faceMatchList = face_recognition.compare_faces(knownEncodings, unknownFaceEncoding)
        #print match list
        #print(faceMatchList)
        for i, value in enumerate(faceMatchList):
            if value:
                fullName = names[i][0] + names[i][1]
                #camera.annotate_text = fullName
                print("I see {}!".format(fullName))
                #camera.annotate_text = fullName
                v.set(fullName)
                createLog(fullName)
                break
            else:
                fullName = "Unknown person"
                v.set(fullName)
        #if (fullName == "Unknown person"):
            #scipy.misc.imsave('./newpeopleimages/outfile.jpg', image)
            #camera.capture('./newpeopleimages/UKNOWN.jpg')
            
    else:
        v.set("")
        #reset annotation
        #camera.annotate_text = ""

    #update GUI
    root.update_idletasks()
    
#if loop breaks - stop camera
camera.stop_preview()
