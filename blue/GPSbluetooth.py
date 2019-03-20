'''
Created by Cayden Pierce Jan. 2019
Receieves data from the "SharedGPS" Android app over Blueooth RFCOMM connection
Location is used as part of the context by which to form memories in the Virtual Memory Assistant
This is loaded by the main program. It runs on a loop, reconnecting if disconnected
'''

#creds to Albert Huang <albert@csail.mit.edu> for some code 

import bluetooth
import pynmea2
from time import sleep
import random

def startBluetoothServer(): #main
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
    print("socket created")
    return sock

def getLocation(sock): #receive data
#         try:
              count = 0 #counts so we don't get an infinite loop if GPS loses its fix
              validNMEA = True
              while (validNMEA and (count < 10)): #finding the data needed to pass to NMEA parser
                  count += 1
                  data = sock.recv(1024)
                  data = data.decode('utf-8')
                  #print('\n')
                  data = data.split('\r')
                  for i, val in enumerate(data[:-1]): #don't scan last in case it isn't complete
                      if val.startswith("$GPGGA"):
                          index = i
                          #print("break")
                          validNMEA = False
                          break
              if (count < 10):
              	parsed = pynmea2.parse(data[index])
              	print("Recieved: ")
              	#print(data[0])
              	return (parsed.latitude, parsed.longitude)
              else:
              	return (["NA","NA"])
        # except Exception:
         #     print("Disconnected, aborting")
          #    #close bluetooth connection
           #   sock.close()
            #  sock = None
