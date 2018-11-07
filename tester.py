import numpy as np
import os
import csv



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
        os.system("cp {} {}".format(("./newpeopleimages/{}".format(file)), ("./knownpeopleimages/{}".format(file))))
        #os.remove("./newpeopleimages/{}".format(file))

        
def loadKnownEncodings():
    knownEncodings = []
    names = []
    peopleDB = [] #this holds the names 
    for i, file in enumerate(os.listdir("./encodings")):
        currentEncoding = openEncoding("./encodings/{}".format(file))
        knownEncodings.append(currentEncoding)
        a = file.partition(".")[0] #remove file extension
        for j, char in enumerate(a[1:]):
            if char.isupper():
                firstName = a[:j+1]
                lastName = a[j+1:]
        names.append([firstName, lastName])
    knownEncodings = np.array(knownEncodings)       
    return knownEncodings, names

#open encoding CSV and create list
def openEncoding(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f, delimiter = ',')
        encoding = list(reader)
        encoding = np.array(encoding[0])
    encoding = encoding.astype(np.float)
    return encoding

print(loadKnownEncodings())
