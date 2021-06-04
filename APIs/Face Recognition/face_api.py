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
    detectedIds : [[SampleNumber, BoundingBox as (x,y,w,h)]] if successul
    Empty List if it fails
    '''
    detectedIds = list()
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    #create request
    sampleNumber = "1"
    r = requests.post(site+"detect", json={"SubscriptionKey": subscriptionKey,                                             
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])   
        print(jsonRes['TTE'])
        if(jsonRes['StatusFlag']==1):    # success
            resultsJson = jsonRes['Result']            
            for result in resultsJson:
                detectedIds.append([result['SampleNumber'], result['BoundingBox']])
                print("SampleNumber ", result['SampleNumber'], " , bbox ", result['BoundingBox'])
            return detectedIds
        else:   # detect fail
            return detectedIds
    else: # invalid response
        return detectedIds
    
def enroll(sampleName, uniqueId, sampleImgFilename, sampleProfileImgFilename):
    '''
    Function to Enroll Face

    Parameters
    ----------
    sampleName : Name of the person getting enrolled
    uniqueId : Unique id for the person getting enrolled
    sampleImgFilename :  Image filename that needs to be enrolled
    sampleProfileImgFilename : Profile image filename for the person for viewing in website (optional)

    Returns
    -------
    detectedIds : [[SampleNumber, StatusMessage]] if successul
    Empty List if it fails
    '''
    enrollStatus = list()
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8') 
    # encode sampleImgArray as base64 image
    sampleProfileImgArray = cv2.cvtColor(numpy.array(Image.open(sampleProfileImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleProfileImgArray) # sampleImgArray as uint8 numpy array
    sampleProfileImg = base64.b64encode(image).decode('utf-8')       
    #create request
    sampleNumber = "1"
    r = requests.post(site+"enroll", json={"SubscriptionKey": subscriptionKey, 
                                           "UniqueId": uniqueId, 
                                           "SampleName": sampleName, 
                                           "SampleProfileImg": sampleProfileImg, 
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])       
        if(jsonRes['StatusFlag']==1):    # success 
            resultsJson = jsonRes['Result']
            for result in resultsJson:
                enrollStatus.append([result['SampleNumber'], result['StatusMessage']])
                print("SampleNumber ", result['SampleNumber'], " , ", result['StatusMessage'])
            return enrollStatus
        else:   # enroll fail
            return enrollStatus
    else: # invalid response
        return enrollStatus

def recognize(sampleImgFilename):
    '''
    Function to Recognize Face

    Parameters
    ----------
    sampleImgFilename : Image of the person

    Returns
    -------
    matchedLst : [[SampleNumber, MatchedName, MatchedId, Confidence, BoundingBox as (x,y,w,h)]] if successul
    Empty List if it fails
    '''
    matchedLst = list()
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    success, image = cv2.imencode('.jpg', sampleImgArray) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    #create request
    sampleNumber = "1"
    r = requests.post(site+"recognize", json={"SubscriptionKey": subscriptionKey,                                             
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])        
        if(jsonRes['StatusFlag']==1):    # success
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
    enrolledIds : [[SampleName(UniqueId)]] if successul
    Empty List if it fails
    '''
    enrolledIds = list()
    r = requests.post(site+"get_enrolls", json={"SubscriptionKey": subscriptionKey})    
    jsonRes = json.loads(r.text)    
    if(r.status_code==200): 
        print(jsonRes['StatusCode'], " : ", jsonRes['StatusMessage'])
        if(jsonRes['StatusFlag']==1):       # success    
            idLst = jsonRes['Result']['Ids']
            for idName in idLst:
                enrolledIds.append(idName['SampleName']+"("+idName['UniqueId']+")")
            print(enrolledIds)                   
    return enrolledIds

# detect
filename = "G:/Datasets/image.jpg" # replace this with your image location
detect(filename)
# enroll
sampleName = "test"
uniqueId = "t01"
sampleImgFilename = filename
sampleProfileImgFilename = filename
enroll(sampleName, uniqueId, sampleImgFilename, sampleProfileImgFilename)
# recognize
recognize(filename)
# get enrolls
get_enrolls()