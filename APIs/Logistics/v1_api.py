# -*- coding: utf-8 -*-
"""
@author: Sacinta

Demo API codes for Sacinta Logistics Manager
1. Go to www.sacinta.com
2. Register an account
3. Get the API key from the API Templates section
3. Use the following functions
"""

## Sample Python Codes for basic funcitons ##
## Python and Android codes for your specific inputs for all the functions avaiable at https://www.sacinta.com/api-templates/logistics ##
import requests
import json
import base64
    
def assetlocations():
    # create json packet to send
    requestJson = {
      "ApiKey": "ENTER_YOUR_API_KEY_HERE"
    }  
    r = requests.post("https://api.sacinta.com/logistics/v1/asset:get_locations", json=requestJson, verify=True) 
    if(r.status_code==200):     
        jsonResponse = json.loads(r.text) 
        print(jsonResponse)     
    else: # invalid response
        print("Invalid response code ", r.status_code)

             
def assetscanImage():
    # convert image to base64 string
    imageBase64 = ""
    with open("ENTER_YOUR_FILENAME_HERE", "rb") as imageFile:
        imageBase64 = base64.b64encode(imageFile.read())
    # create json packet to send
    requestJson = {
        "Asset": {
            "data1": {
                "AssetImage": imageBase64,
                "ScanType": "drop",
                "ScanTimeUTC": "2023-02-12 14:42:00",
                "LocationId": 8
            }
        },
        "ApiKey": "ENTER_YOUR_API_KEY_HERE"
    } 
    r = requests.post("https://api.sacinta.com/logistics/v1/asset:scan", json=requestJson, verify=True) 
    if(r.status_code==200):     
        jsonResponse = json.loads(r.text) 
        print(jsonResponse)     
    else: # invalid response
        print("Invalid response code ", r.status_code)

def assetscanCode():
    # convert image to base64 string
    imageBase64 = ""
    with open("ENTER_YOUR_FILENAME_HERE", "rb") as imageFile:
        imageBase64 = base64.b64encode(imageFile.read())
    # create json packet to send
    requestJson = {
        "Asset": {
            "data1": {
                "AssetCode": "12987689765432"
                "ScanType": "drop",
                "ScanTimeUTC": "2023-02-12 14:42:00",
                "LocationId": 8
            }
        },
        "ApiKey": "ENTER_YOUR_API_KEY_HERE"
    } 
    r = requests.post("https://api.sacinta.com/logistics/v1/asset:scan", json=requestJson, verify=True) 
    if(r.status_code==200):     
        jsonResponse = json.loads(r.text) 
        print(jsonResponse)     
    else: # invalid response
        print("Invalid response code ", r.status_code)
        
              
def sendlivetracking():
    # create json packet to send
    requestJson = {
        "LocationData": {
            "data1": {
                "RouteUUID": "123456",
                "LocationLat": 17.56,
                "LocationLong": 78.23,
                "LocationAccuracy": 50,
                "Speed": 10,
                "Altitude": 560,
                "AltitudeAccuracy": 10
            }
      },
      "ApiKey": "ENTER_YOUR_API_KEY_HERE"
    }
    r = requests.post("https://api.sacinta.com/logistics/v1/track:send_live_tracking", json=requestJson, verify=True) 
    if(r.status_code==200):     
        jsonResponse = json.loads(r.text) 
        print(jsonResponse)     
    else: # invalid response
        print("Invalid response code ", r.status_code)
