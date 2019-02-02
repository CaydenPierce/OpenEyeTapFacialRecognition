import csv
import datetime as dt

def CurrentTime():
    return('%s')%(dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

def createLog(name): #adds log of seeing person. Contains context such as who, what, where, when
        with open("./memory/lifelog.csv", "a", newline="") as log_csv: #open in append and read mode
            time = CurrentTime()
            location = GPSbluetooth.getLocation(sock)
            memory = [time, location, name]
            wr = csv.writer(log_csv, delimiter = ',')
            wr.writerow(memory)

createLog("Cayden Pierce")
