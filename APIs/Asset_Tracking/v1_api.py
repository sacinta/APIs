# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:07:34 2021

@author: Ram
"""

# -*- coding: utf-8 -*-
"""
@author: Sacinta

Demo API codes for Sacinta Face Recognition
1. Go to www.sacinta.com
2. Register an account
3. Go to Subscriptions Menu and copy a Subscription Key
4. Use the following functions to detect, enroll, recognize and read ids in your database
"""

import requests
import base64
from cv2 import *
import numpy
from PIL import Image
import json
from io import BytesIO
import matplotlib.pyplot as plt
import datetime

site = "http://127.0.0.1:5000/asset/v1/"#"https://sacinta.com/face/"#
# set the SubsriptionKey from Subscription Page
apiKey = "b45a33f34fab4b139dbdb5126782e536"#"8927f86599874bfb95a464351d53146c"#

def track_get_locations():
    print("\n------------------ track_get_locations -----------------------")
    r = requests.post(site+"track:get_locations", json={"ApiKey": apiKey}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        print("\n------------------ Result JSON -----------------------")
        print(jsonRes['Result'])
        dummy=0
    else: # invalid response
        print(r.status_code)
        
def track_scan_asset(sampleImgFilename):
    print("\n------------------ track_scan_asset -----------------------")
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    # create request
    sampleNumber = "1"
    inputDict = {"AssetImage":sampleImg,"LocationLat":"135.256","LocationLong":"-256.135", "LocationId":"8","ScanType":"Drop"}
    
    r = requests.post(site+"track:scan_asset", json={"ApiKey": apiKey,                                             
                                           "Asset":{"1":inputDict}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        print("\n------------------ Result JSON -----------------------")
        print(jsonRes['Result'])
        dummy=0
    else: # invalid response
        print(r.status_code)

def track_send_live_tracking():
    print("\n------------------ send_live_tracking -----------------------")
    locationData = {"RouteUUID":"1234",
                    "LocationLat":'6.05', 
                    "LocationLong":'0.135', 
                    "LocationId":8,
                    "LogTimeUTC":str(datetime.date.today()), 
                    "LocationAccuracy":0, 
                    "Speed":1, 
                    "Altitude":1, 
                    "AltitudeAccuracy":1}
    r = requests.post(site+"track:send_live_tracking", json={"ApiKey": apiKey,
                                                             "LocationData" : {'1':locationData}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        print("\n------------------ Result JSON -----------------------")
        print(jsonRes['Result'])
        dummy=0
    else: # invalid response
        print(r.status_code)

def admin_current_asset_status():
    print("\n------------------ admin_current_asset_status -----------------------")
    r = requests.post(site+"admin:current_asset_status", json={"ApiKey": apiKey}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        print("\n------------------ Result JSON -----------------------")
        print(jsonRes['Result'])
        dummy=0
    else: # invalid response
        print(r.status_code) 

def admin_manage_asset(sampleImgFilename):
    print("\n------------------ track_scan_asset -----------------------")
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    # create request
    sampleNumber = "1"
    inputDict = {"AssetImage":sampleImg,"AssetAction":"Add"}
    
    r = requests.post(site+"admin:manage_asset", json={"ApiKey": apiKey,                                             
                                           "Asset":{"1":inputDict}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        print("\n------------------ Result JSON -----------------------")
        print(jsonRes['Result'])
        dummy=0
    else: # invalid response
        print(r.status_code)
        
track_get_locations()        
track_scan_asset("C:/Users/Ram/Desktop/qr1.jfif")
track_send_live_tracking()
admin_current_asset_status()
admin_manage_asset("C:/Users/Ram/Desktop/qr1.jfif")
