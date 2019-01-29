'''
Created by Cayden Pierce Jan. 2019
Receieves data from the "SharedGPS" Android app over Blueooth RFCOMM connection
Location is used as part of the context by which to form memories in the Virtual Memory Assistant
'''

#creds to Albert Huang <albert@csail.mit.edu> for some code 

import bluetooth
import pynmea2

target = None
#check for visible devices (do-while loop)
while True:
     services = bluetooth.find_service(address=target)
     if (len(services) > 0):
          break
     print("No services found. Try again")

#find address and port that contains ShareGPS stuffs
for svc in services:
     if "ShareGPS" == svc["name"]:
          host = svc["host"]
          port=svc["port"]


# Create the client socket
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((host, port))

#receive data
counter = 0
while counter < 99:
     try:
          data = sock.recv(1024)
          data = data.decode('utf-8')
          data = data.split('\r')
          parsed = pynmea2.parse(data[0])
          print("Recieved: ")
          #print(data[0])
          print("Latitude: " + str(parsed.latitude) + " Longitude: " + str(parsed.longitude))
          counter += 1
     except Exception:
          print("Disconnected, aborting")
          break

#close bluetooth connection
sock.close()
         
