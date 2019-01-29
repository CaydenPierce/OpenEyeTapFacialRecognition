'''
Created by Cayden Pierce Jan. 2019
Receieves data from the "SharedGPS" Android app over Blueooth RFCOMM connection
Location is used as part of the context by which to form memories in the Virtual Memory Assistant
'''

#creds to Albert Huang <albert@csail.mit.edu> for some code 

import bluetooth


#check for visible devices
while (len(services) = 0):
     services = bluetooth.find_service()
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
while counter < 5:
     data = sock.recv(1024)
     print("Recieved: ")
     print(data)
     counter += 1

#close bluetooth connection
sock.close()
         
