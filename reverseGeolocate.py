import requests
import json

def getAddress(lat, long):
    try:
        url = "https://nominatim.openstreetmap.org/reverse?format=json&lat={}&lon={}&zoom=18&addressdetails=1".format(lat, long)
        response = requests.get(url)
        data= response.json()
        house_number = data['address']['house_number']
        road = data['address']['road']
        city = data['address']['city']
        return data['display_name']
    except Exception:
        return ("Latitude: " + lat + " Longitude: " + long)
    

print(getAddress("42.994813683333334", "-555.26322528333333"))
