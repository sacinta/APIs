# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 19:52:10 2021

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

site = "http://127.0.0.1:5000/asset/v1/"#"https://sacinta.com/face/"#
# set the SubsriptionKey from Subscription Page
apiKey = "b45a33f34fab4b139dbdb5126782e536"#"8927f86599874bfb95a464351d53146c"#

def detect(sampleImgFilename):
    '''
    Function to detect face(s) in the image filename

    Parameters
    ----------
    sampleImgFilename : Image filename

    Returns
    -------
    Result : [[SampleNumber, BoundingBox as (x,y,w,h)]] if successul
    Empty List if it fails
    '''
    detectedIds = list()
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    # create request
    sampleNumber = "1"
    r = requests.post(site+"detect", json={"ApiKey": apiKey,                                             
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes)
        print(jsonRes['ResponseCode'], " , ", jsonRes['ResponseMessage'])   
        if(jsonRes['ResponseFlag']==1):    # success
            print("Time To Execute: ", jsonRes['TTE'])
            resultsJson = jsonRes['Result']            
            for result in resultsJson:
                detectedIds.append([result['SampleNumber'], result['BoundingBox']])
                print("SampleNumber ", result['SampleNumber'], " , bbox ", result['BoundingBox'])
            return detectedIds
        else:   # detect fail            
            return detectedIds
    else: # invalid response
        return detectedIds
    
def enroll(sampleName, uniqueId, sampleImgFilenameLst, sampleProfileImgFilename):
    '''
    Function to Enroll Face

    Parameters
    ----------
    sampleName : Name of the person getting enrolled
    uniqueId : Unique id for the person getting enrolled
    sampleImgFilenameLst :  List of image filenames that needs to be enrolled
    sampleProfileImgFilename : Profile image filename for the person for viewing in website (optional)

    Returns
    -------
    Result : [[SampleNumber, ResponseMessage]] if successul
    Empty List if it fails
    '''
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
        print(jsonRes['ResponseCode'], " , ", jsonRes['ResponseMessage'])       
        if(jsonRes['ResponseFlag']==1):    # success 
            print("Time To Execute: ", jsonRes['TTE'])
            resultsJson = jsonRes['Result']
            for result in resultsJson:
                enrollStatus.append([result['SampleNumber'], result['ResultMessage']])
                print("SampleNumber ", result['SampleNumber'], " , ", result['ResultMessage'])
            return enrollStatus
        else:   # enroll fail
            return enrollStatus
    else: # invalid response
        return enrollStatus

def recognize(sampleImgFilenameLst):
    '''
    Function to Recognize Face

    Parameters
    ----------
    sampleImgFilenameLst : Image of the person

    Returns
    -------
    Result : [[SampleNumber, MatchedName, MatchedId, Confidence, BoundingBox as (x,y,w,h)]] if successul
    Empty List if it fails
    '''
    matchedLst = list()   
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
                                           "SampleImages": sampleImagesDict})#{sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['ResponseCode'], " , ", jsonRes['ResponseMessage'])            
        if(jsonRes['ResponseFlag']==1):    # success
            print("Time To Execute: ", jsonRes['TTE'])
            resultsJson = jsonRes['Result']            
            for result in resultsJson:
                print("SampleNumber ", result['SampleNumber'], " ,MatchedName ", result['MatchedName'], " ,Matched Id ", result['MatchedId'], " ,Confidence ", result['Confidence']," ,bbox ", result['BoundingBox'])        
                matchedLst.append([result['SampleNumber'],result['MatchedName'],result['MatchedId'],result['Confidence'],result['BoundingBox']])
            print(matchedLst)
            return matchedLst
        else:   # recognize fail
            return matchedLst
    else: # invalid response
        return matchedLst

def get_enrolls():
    '''
    Function to retrieve all the enrolled Ids in the database
    
    Returns
    -------
    Result : [[SampleName(UniqueId)]] if successul
    Empty List if it fails
    '''
    enrolledIds = list()
    r = requests.post(site+"get_enrolls", json={"ApiKey": apiKey}) 
    from datetime import datetime
    scanTime = datetime.utcnow().timestamp()
# =============================================================================
#     r = requests.post("http://127.0.0.1:5000/asset/track", json={"ApiKey": "b22c5f0da9a34185ac3da0f0bb2346a2",
#                                                                  "Asset":{1:{"AssetCode": int(scanTime),
#                                                                           "LocationId":8,"LocationLat":52.07,"LocationLong":17.06,
#                                                                           "ScanType":"Drop", "ScanTimeUTC":scanTime},
#                                                                           2:{"AssetCode": int(datetime.utcnow().timestamp()),
#                                                                           "LocationId":8,"LocationLat":52.07,"LocationLong":17.06,
#                                                                           "ScanType":"Drop", "ScanTimeUTC":scanTime}}
#                                                                  })    
# =============================================================================
# =============================================================================
#     r = requests.post("http://127.0.0.1:5000/asset/track", json={"ApiKey":"b22c5f0da9a34185ac3da0f0bb2346a2",
#                                                                   "Asset":{"1628525440138-1":{"AssetCode":"036000291452-1","LocationId":8,"LocationLat":12.9501196,"LocationLong":80.1953591,"ScanType":"Pick","ScanTimeUTC":"2021-08-09 21:40:40"},
#                                                                            "1628525569571-1":{"AssetCode":"036000291452-2","LocationId":8,"LocationLat":0,"LocationLong":0,"ScanType":"Pick","ScanTimeUTC":"2021-08-09 21:41:40.138000"},
#                                                                            "1628567449430-1":{"AssetCode":"036000291452-3","LocationId":8,"LocationLat":0,"LocationLong":0,"ScanType":"Drop","ScanTimeUTC":"2021-08-09 21:42:40.138000"}}}
#                                                                   )
# =============================================================================
    #r = requests.post("http://127.0.0.1:5000/asset/locations", json={"ApiKey":"a2f2b09554d740e585298e02637047ad"})
    #r = requests.post("http://127.0.0.1:5000/user_info", json={"ApiKey":"b22c5f0da9a34185ac3da0f0bb2346a2","Asset":{"1629439482765":{"AssetCode":"5012345678900","LocationId":28,"LocationLat":12.950107,"LocationLong":80.1953913,"ScanType":"Pick","ScanTimeUTC":1629439482765}}})
    #r = requests.post("http://127.0.0.1:5000/asset/track", json={"ApiKey":"b22c5f0da9a34185ac3da0f0bb2346a2"})
    #print('scanTime ', scanTime)
    #r = requests.post("http://127.0.0.1:5000/asset/android_version")
    print(r.status_code)
    if(r.status_code==200): 
        jsonRes = json.loads(r.text)  
        print(jsonRes['ResponseCode'], " , ", jsonRes['ResponseMessage'])
        if(jsonRes['ResponseFlag']==1):       # success 
            print("Time To Execute: ", jsonRes['TTE'])
            idLst = jsonRes['Result']['Ids']
            for idName in idLst:
                enrolledIds.append([idName['SampleName'],idName['UniqueId']])
            print(enrolledIds)                   

# =============================================================================
#     r = requests.post("http://127.0.0.1:5000/asset/live_tracking", json={"ApiKey": "b22c5f0da9a34185ac3da0f0bb2346a2",
#                                                                  "LocationData":{1:{"LocationLat":52.07,"LocationLong":17.06,
#                                                                           "Speed":0, "LogTimeUTC":scanTime},
#                                                                           2:{"LocationLat":52.08,"LocationLong":17.07,
#                                                                           "Speed":0, "LogTimeUTC":scanTime}}
#                                                                  })    
#     print(r.status_code)
#     if(r.status_code==200): 
#         jsonRes = json.loads(r.text)  
#         print(jsonRes)        
# =============================================================================
            
    return enrolledIds

def remove(removeIdsList):
    '''
    Function to Remove Enrolled Ids

    Parameters
    ----------
    removeIdsList : List of ids to be removed obtained from get_enrolls containing unique ids

    Returns
    -------
    Result : [[SampleUniqueId, ResponseMessage]] if successul
    Empty List if it fails
    '''    
    # create dictionary with all the ids to be removed. To get list of ids, use get_enrolls
    uniqueIdsDict = {}
    for sampleIndex in range(len(removeIdsList)):
        uniqueIdsDict[str(sampleIndex+1)] = removeIdsList[sampleIndex]
    # create request
    r = requests.post(site+"remove_enrolls", json={"ApiKey": apiKey,                                             
                                           "UniqueIds": uniqueIdsDict}) 
    deletedLst = []
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['ResponseCode'], " , ", jsonRes['ResponseMessage'])        
        if(jsonRes['ResponseFlag']==1):    # success 
            print("Time To Execute: ", jsonRes['TTE'])
            resultsJson = jsonRes['Result']
            for result in resultsJson:
                print("SampleUniqueId ", result['SampleUniqueId'], " ,ResponseMessage ", result['ResultMessage'])        
                deletedLst.append([result['SampleUniqueId'],result['ResultMessage']])             
            return deletedLst            
        else:   # delete fail            
            return jsonRes['ResponseMessage']
    else: # invalid response
        return "Error"

# =============================================================================
# # detect
# filename = "G:/Work/Sacinta/project/static/blog_assets/face-recognition/simon-helberg.jpg"#"test-image.jpg"#"C:/Users/Ram/Desktop/thumbs-down.png"#"G:/Datasets/image.jpg" # replace this with your image location
# # detect
# detect(filename)
# # enroll
# sampleName = "test"
# uniqueId = "t01"
# sampleImgFilenameLst = [filename] # create a list of all the filenames you want to enroll
# sampleProfileImgFilename = filename
# enroll(sampleName, uniqueId, sampleImgFilenameLst, sampleProfileImgFilename)
# # recognize
# sampleImgFilenameLst = [filename] # create a list of all the filenames you want to recognize
# recognize(sampleImgFilenameLst)
# # get all enrolled ids
# enrolledIds = get_enrolls()
# # Remove enrolled id
# removeIdsList = "t01"#enrolledIds[0][1] # unqiue id of the 1st name enrolled
# remove([removeIdsList])
# =============================================================================
