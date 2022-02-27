# -*- coding: utf-8 -*-
"""
@author: Sacinta

Demo API codes for Sacinta Logistics Manager
1. Go to www.sacinta.com
2. Register an account
3. Get the API key from the Profile section
3. Use the following functions
"""

import requests
import base64
from cv2 import *
import numpy
from PIL import Image
import json
from io import BytesIO
import datetime

site = "https://api.sacinta.com/logistics/v1/"
apiKey = "get api key from subscription page and paste here"

def track_get_locations():
    print("\n------------------ track_get_locations -----------------------")
    r = requests.post(site+"asset:get_locations", json={"ApiKey": apiKey}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        if 'Result' in jsonRes:
            print("\n------------------ Result JSON -----------------------")
            print(jsonRes['Result'])     
    else: # invalid response
        print(r.status_code)
    r.close()
        
def track_scan_asset(sampleImgFilename):
    print("\n------------------ track_scan_asset -----------------------")
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    # create request
    sampleNumber = "1"
    inputDict = {"AssetImage":sampleImg,"LocationLat":"135.256","LocationLong":"-256.135", "LocationId":"8","ScanType":"Drop", "ScanTimeUTC":"2022-02-09 10:11:45.2"}
    
    r = requests.post(site+"asset:scan", json={"ApiKey": apiKey,                                             
                                           "Asset":{"1":inputDict}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        if 'Result' in jsonRes:
            print("\n------------------ Result JSON -----------------------")
            print(jsonRes['Result'])        
    else: # invalid response
        print(r.status_code)
    r.close()

def admin_current_asset_status():
    print("\n------------------ admin_current_asset_status -----------------------")
    r = requests.post(site+"admin:asset:current_status", json={"ApiKey": apiKey}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        if 'Result' in jsonRes:
            print("\n------------------ Result JSON -----------------------")
            print(jsonRes['Result'])       
    else: # invalid response
        print(r.status_code) 
    r.close()

def admin_manage_asset(sampleImgFilename):
    print("\n------------------ track_scan_asset -----------------------")
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    # create request
    sampleNumber = "1"
    inputDict = {"AssetImage":sampleImg,"AssetAction":"Add"}
    
    r = requests.post(site+"admin:asset:manage", json={"ApiKey": apiKey,                                             
                                           "Asset":{"1":inputDict}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes) 
        if 'Result' in jsonRes:
            print("\n------------------ Result JSON -----------------------")
            print(jsonRes['Result'])       
    else: # invalid response
        print(r.status_code)
    r.close()
        
track_get_locations()        
track_scan_asset("barcode.png") # replace with image location
admin_current_asset_status()
admin_manage_asset("barcode.png")   # replace with image location
