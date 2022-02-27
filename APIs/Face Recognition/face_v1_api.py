"""
@author: Sacinta

Demo API codes for Sacinta Face Recognition
1. Go to www.sacinta.com
2. Register an account
3. Get the API Key from the Profile section
4. Use the following functions to detect, enroll, recognize, get and remove enrolls
"""

import requests
import base64
from cv2 import *
import numpy
from PIL import Image
import json
from io import BytesIO

site = "https://api.sacinta.com/face/v1/"
apiKey = "get api key from subscription page and paste here"

def detect(sampleImgFilenameLst): 
    print("\n------------------ detect -----------------------")    
    # read filenames and encode sampleImgArray as base64 image    
    sampleImagesDict = {}
    for sampleIndex in range(len(sampleImgFilenameLst)):
        # read sampleImgFilename and encode sampleImgArray as base64 image    
        sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilenameLst[sampleIndex])), cv2.COLOR_BGR2RGB)
        success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
        sampleImg = base64.b64encode(image).decode('utf-8') 
        sampleImagesDict[str(sampleIndex+1)] = sampleImg
                 
    # create request    
    r = requests.post(site+"detect", json={"ApiKey": apiKey,                                             
                                           "SampleImages": sampleImagesDict}) 
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
    
def enroll(sampleName, uniqueId, sampleImgFilenameLst, sampleProfileImgFilename):
    print("\n------------------ enroll -----------------------")    
    enrollStatus = list()    
    # encode sampleImgArray as base64 image
    sampleProfileImgArray = cv2.cvtColor(numpy.array(Image.open(sampleProfileImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleProfileImgArray) # sampleImgArray as uint8 numpy array
    sampleProfileImg = base64.b64encode(image).decode('utf-8')  
    # create dictionary with all the SampleImages, you can enroll multiple images at the same time
    sampleImagesDict = {}
    for sampleIndex in range(len(sampleImgFilenameLst)):
        # read sampleImgFilename and encode sampleImgArray as base64 image    
        sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilenameLst[sampleIndex])), cv2.COLOR_BGR2RGB)
        success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
        sampleImg = base64.b64encode(image).decode('utf-8') 
        sampleImagesDict[str(sampleIndex+1)] = sampleImg        
        
    # create request    
    r = requests.post(site+"enroll", json={"ApiKey": apiKey, 
                                           "UniqueId": uniqueId, 
                                           "SampleName": sampleName, 
                                           "SampleProfileImg": sampleProfileImg, 
                                           "SampleImages": sampleImagesDict})     
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

def recognize(sampleImgFilenameLst):
    print("\n------------------ recognize -----------------------")    
    # create dictionary with all the SampleImages, you can recognize multiple images at the same time
    sampleImagesDict = {}
    for sampleIndex in range(len(sampleImgFilenameLst)):
        # read sampleImgFilename and encode sampleImgArray as base64 image    
        sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilenameLst[sampleIndex])), cv2.COLOR_BGR2RGB)
        success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
        sampleImg = base64.b64encode(image).decode('utf-8') 
        sampleImagesDict[str(sampleIndex+1)] = sampleImg
    
    #create request 
    r = requests.post(site+"recognize", json={"ApiKey": apiKey,                                             
                                              "SampleImages": sampleImagesDict})
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

def get_enrolls():
    print("\n------------------ get_enrolls -----------------------")    
    enrolledIds = list()
    r = requests.post(site+"get_enrolls", json={"ApiKey": apiKey})    
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

def remove(removeIdsList): 
    print("\n------------------ remove -----------------------")    
    # create dictionary with all the ids to be removed. To get list of ids, use get_enrolls
    uniqueIdsDict = {}
    for sampleIndex in range(len(removeIdsList)):
        uniqueIdsDict[str(sampleIndex+1)] = removeIdsList[sampleIndex]
        
    # create request
    r = requests.post(site+"remove_enrolls", json={"ApiKey": apiKey,                                             
                                           "UniqueIds": uniqueIdsDict})     
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

filename = "test-image.jpg"# replace this with your image location
sampleImgFilenameLst = [filename, filename] # create a list of all the filenames

# detect
detect(sampleImgFilenameLst)

# enroll
sampleName = "test"
uniqueId = "t01"
sampleProfileImgFilename = filename
enroll(sampleName, uniqueId, sampleImgFilenameLst, sampleProfileImgFilename)

# recognize
sampleImgFilenameLst = [filename] # create a list of all the filenames you want to recognize
recognize(sampleImgFilenameLst)

# get all enrolled ids
enrolledIds = get_enrolls()

# Remove enrolled id
removeIdsList = "t01"
remove([removeIdsList])
