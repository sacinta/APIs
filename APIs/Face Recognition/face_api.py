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

site = "https://www.sacinta.com/face/"
# set the SubsriptionKey from Subscription Page
subscriptionKey = "xxxxxxxxxxxxxxxxxxxxx"

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
    r = requests.post(site+"detect", json={"SubscriptionKey": subscriptionKey,                                             
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text) 
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])   
        if(jsonRes['StatusFlag']==1):    # success
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
    Result : [[SampleNumber, StatusMessage]] if successul
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
    r = requests.post(site+"enroll", json={"SubscriptionKey": subscriptionKey, 
                                           "UniqueId": uniqueId, 
                                           "SampleName": sampleName, 
                                           "SampleProfileImg": sampleProfileImg, 
                                           "SampleImages": sampleImagesDict})     
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])       
        if(jsonRes['StatusFlag']==1):    # success 
            print("Time To Execute: ", jsonRes['TTE'])
            resultsJson = jsonRes['Result']
            for result in resultsJson:
                enrollStatus.append([result['SampleNumber'], result['StatusMessage']])
                print("SampleNumber ", result['SampleNumber'], " , ", result['StatusMessage'])
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
    r = requests.post(site+"recognize", json={"SubscriptionKey": subscriptionKey,                                             
                                           "SampleImages": sampleImagesDict})#{sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])            
        if(jsonRes['StatusFlag']==1):    # success
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
    r = requests.post(site+"get_enrolls", json={"SubscriptionKey": subscriptionKey})    
    jsonRes = json.loads(r.text)    
    if(r.status_code==200): 
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])
        if(jsonRes['StatusFlag']==1):       # success 
            print("Time To Execute: ", jsonRes['TTE'])
            idLst = jsonRes['Result']['Ids']
            for idName in idLst:
                enrolledIds.append([idName['SampleName'],idName['UniqueId']])
            print(enrolledIds)                   
    return enrolledIds

def remove(removeIdsList):
    '''
    Function to Remove Enrolled Ids

    Parameters
    ----------
    removeIdsList : List of ids to be removed obtained from get_enrolls containing unique ids

    Returns
    -------
    Result : [[SampleUniqueId, StatusMessage]] if successul
    Empty List if it fails
    '''    
    # create dictionary with all the ids to be removed. To get list of ids, use get_enrolls
    uniqueIdsDict = {}
    for sampleIndex in range(len(removeIdsList)):
        uniqueIdsDict[str(sampleIndex+1)] = removeIdsList[sampleIndex]
    # create request
    r = requests.post(site+"remove", json={"SubscriptionKey": subscriptionKey,                                             
                                           "UniqueIds": uniqueIdsDict}) 
    deletedLst = []
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])        
        if(jsonRes['StatusFlag']==1):    # success 
            print("Time To Execute: ", jsonRes['TTE'])
            resultsJson = jsonRes['Result']
            for result in resultsJson:
                print("SampleUniqueId ", result['SampleUniqueId'], " ,StatusMessage ", result['StatusMessage'])        
                deletedLst.append([result['SampleUniqueId'],result['StatusMessage']])             
            return deletedLst            
        else:   # delete fail            
            return jsonRes['StatusMessage']
    else: # invalid response
        return "Error"

# detect
filename = "G:/Datasets/image.jpg" # replace this with your image location
detect(filename)
# enroll
sampleName = "test"
uniqueId = "t01"
sampleImgFilenameLst = [filename] # create a list of all the filenames you want to enroll
sampleProfileImgFilename = filename
enroll(sampleName, uniqueId, sampleImgFilenameLst, sampleProfileImgFilename)
# recognize
sampleImgFilenameLst = [filename] # create a list of all the filenames you want to recognize
recognize(sampleImgFilenameLst)
# get all enrolled ids
enrolledIds = get_enrolls()
# Remove enrolled id
removeIdsList = enrolledIds[0][1] # unqiue id of the 1st name enrolled
remove([removeIdsList])
