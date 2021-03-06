# -*- coding: utf-8 -*-
"""
@author: Sacinta

Demo API codes for Sacinta Mobile Robotics
1. Go to www.sacinta.com
2. Register an account
3. Go to Subscriptions Menu and create a Demo Subscription
4. Use the following functions for object detection and obstacle avoidance
"""

import requests
import base64
from cv2 import *
import numpy
from PIL import Image
import json
from io import BytesIO
import matplotlib.pyplot as plt

site = "https://www.sacinta.com/mobilerobo/"
# set the SubsriptionKey from Subscription Page
subscriptionKey = "xxxxxxxxxxxxxxxxxxxxx"

def objectDetection(sampleImgFilename):
    '''
    Function to detect Objects in the image filename

    Parameters
    ----------
    sampleImgFilename : Image filename

    Returns
    -------
    objectMapLst : [RGB Image for detected objects] if successul
    Empty List if it fails
    '''
    objectMapLst = list()
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    # resize image to speed up processing (optional, default = 1)
    divFactor = 0.5
    sampleImgArray = cv2.resize(sampleImgArray, (0,0), fx=divFactor, fy=divFactor)
    # jpeg encode factor, default is 95
    success, image = cv2.imencode('.jpg', sampleImgArray,[int(cv2.IMWRITE_JPEG_QUALITY), 95]) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    #create request
    sampleNumber = "1"
    r = requests.post(site+"obstacle", json={"SubscriptionKey": subscriptionKey,                                             
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])
        print(jsonRes['TTE'])        
        if(jsonRes['StatusFlag']==1):    # success            
            resultsJson = jsonRes['Result']            
            for result in resultsJson:
                mapImage = numpy.array(Image.open(BytesIO(base64.b64decode(result['ImageBase64']))))                
                plt.imshow(mapImage)
                plt.show()
                objectMapLst.append(mapImage)                
            return objectMapLst
        else:   # detect fail
            return objectMapLst            
    else: # invalid response
        return objectMapLst
    
def obstacleAvoidance(sampleImgFilename, minSafeDistFact, minObjHeigthFact, minObjWidthFact, minPathWidthFact):
    '''
    Function to detect Objects in the image filename

    Parameters
    ----------
    sampleImgFilename : Image filename
    minSafeDistFact: minimum safe distance between object and rover as a factor of image row size
    maxObjHeigthFact: maximum object height as a factor of image row size
    minPathWidthFact: minimum path width as a factor of image column size
    
    Returns
    -------
    objectMapLst : [RGB Image for detected objects] if successul
    Empty List if it fails
    '''
    bestAngleLst = list()
    # read sampleImgFilename and encode sampleImgArray as base64 image    
    sampleImgArray = cv2.cvtColor(numpy.array(Image.open(sampleImgFilename)), cv2.COLOR_BGR2RGB)
    # resize image to speed up processing (optional)
    divFactor = 0.5
    sampleImgArray = cv2.resize(sampleImgArray, (0,0), fx=divFactor, fy=divFactor)
    # jpeg encode factor, default is 95
    success, image = cv2.imencode('.jpg', sampleImgArray,[int(cv2.IMWRITE_JPEG_QUALITY), 95]) # sampleImgArray as uint8 numpy array
    sampleImg = base64.b64encode(image).decode('utf-8')      
    #create request
    sampleNumber = "1"    
    start = timer() 
    site = "https://www.sacinta.com"    
    r = requests.post(site+"obstacle_avoidance_basic", json={"SubscriptionKey": subscriptionKey,                                             
                                           "MinSafeDistanceFactor":minSafeDistFact,
                                           "MinPathWidthFactor":minPathWidthFact,
                                           "MinObjectHeightFactor":minObjHeigthFact,
                                           "MinObjectWidthFactor":minObjWidthFact,                                           
                                           "SaveFileId":"1",
                                           "SampleImages": {sampleNumber:sampleImg}}) 
    print('tte ', timer()-start)
    # check response
    if(r.status_code==200):                
        jsonRes = json.loads(r.text)
        print(jsonRes)
        print(jsonRes['StatusCode'], " , ", jsonRes['StatusMessage'])
        print(jsonRes['TTE'])        
        if(jsonRes['StatusFlag']==1):    # success            
            resultsJson = jsonRes['Result']            
            for result in resultsJson:
                print(result['StatusMessage'])                    
                bestDirectionAngle = (result['BestDirectionAngle'])+90
                maxDistanceFactor = result['MaxDistanceFactor']
                maxWidthFactor = result['MaxPathWidthFactor']                
                plt.imshow(image)
                plt.show()
                bestAngleLst.append(bestDirectionAngle)                
            return bestAngleLst
        else:   # detect fail
            return bestAngleLst            
    else: # invalid response
        return bestAngleLst
        

# obstacle detection
sampleImgFilename = "G:/Datasets/image.jpg" # replace this with your image location
objectDetection(sampleImgFilename)
# obstacle avoidance
minSafeDistFact = 0.5
minPathWidthFact = 0.3
minObjHeigthFact = 0.1
minObjWidthFact = 0.1
obstacleAvoidance(sampleImgFilename, minSafeDistFact, minObjHeigthFact, minObjWidthFact, minPathWidthFact)