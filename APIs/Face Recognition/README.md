# Face Recognition APIs
Python APIs for Face Recognition services

You can access four services using the python APIs
1. detect - detects faces and returns bounding boxes for each face
2. enroll - enrolls a face. The image must contain only one straight face, you'll need to give the sample name and unique id associated with the face
3. recognize - recognize upto 3 faces in the given image and return the sample name and unique id for each associated name
4. get_enrolls - get the sample names and unqiue ids for enrolled samples

# Detect
url: https://www.sacinta.com/face/detect
request:
{
    "SubscriptionKey": "<Subscription Key>",
    "SampleImages": {
        "1": "<SampleImage in base 64 format>",        
    }
}

response:
{	
	"Result": [["image_number","BoundingBox","Confidence","StatusCode","StatusMessage"]],
    "StatusFlag": "<Status:1 if atleast 1 face is detected, 0 if no face detected, -1 for input error>",
    "StatusCode": "[SUCCESS, FAIL, MISSING_SUBSRIPTION_KEY, MISSING_SAMPLE_IMAGE, INVALID_SUBSRIPTION_KEY, INVALID_USER, INVALID_GALLERY, INVALID_ID_NAME, FACE_NOT_STRAIGHT]",
    "StatusMessage": "<a message description>",
	"Version": "version number",
	"TTE": "time to execute in seconds"
} 

# enroll
url: https://www.sacinta.com/face/enroll
request:
{
    "SubscriptionKey": "<Subscription Key>",
	"SampleName": "Enroll Id Name",
    "UniqueId": "Unique Id for Enroll Id Name", 	
    "SampleProfileImg": "profile image in base 64 format for displaying thumbnail on website",
    "SampleImages": {
        "1": "<SampleImages in base 64 format>",        
    }
}

response:
{	
	"Result": [["image_number"", "StatusCode", "StatusMessage", "StatusMessage"]],
    "StatusFlag": "<Status:1 for success, 0 fail, -1 error>",
    "StatusCode": "[SUCCESS, FAIL_MULTIPLE_FACES_DETECTED, FAIL_FACE_NOT_DETECTED, FAIL_FACE_NOT_STRAIGHT, FAIL_FACE_SIZE_SMALL, MISSING_SUBSRIPTION_KEY, MISSING_SAMPLE_IMAGE, MISSING_SAMPLE_NAME, MISSING_UNIQUE_ID, INVALID_SUBSRIPTION_KEY, DUPLICATE_ENROLL, INVALID_SAMPLE_NAME, INVALID_UNIQUE_ID, INVALID_USER, INVALID_GALLERY]",
    "StatusMessage": "<a message desccription>",
	"Version": "version number",
	"TTE": "time to execute in seconds"
}

# recognize
url: https://www.sacinta.com/face/recognize
request:
{
    "SubscriptionKey": "<Subscription Key>",
	"Gallery": "Gallery Name",
    "SampleImages": {
        "1": "<SampleImage in base 64 format>",        
    }
}

respose:
{	
	"Result": [["image_number","BoundingBox","SampleName","UniqueId","Confidence","StatusCode","StatusMessage","MatchScore"]],
    "StatusFlag": "<Status:1 if atleast 1 face is recognized, 0 if no face recognized, -1 for input error>",
    "StatusCode": "[SUCCESS, FAIL_FACE_NOT_DETECTED, FAIL_FACE_NOT_STRAIGHT, FAIL_FACE_SIZE_SMALL, FAIL_FACE_NOT_RECOGNIZED, MISSING_SUBSRIPTION_KEY, MISSING_SAMPLE_IMAGE, INVALID_SUBSRIPTION_KEY, INVALID_USER, GALLERY_EMPTY, DATABASE_EMPTY]",
    "StatusMessage": "<a message desccription>",
	"Version": "version number",
	"TTE": "time to execute in seconds"
} 

# get enrolls
url: https://www.sacinta.com/face/get_enrolls
request:
{
    "SubscriptionKey": "<Subscription Key>",    
}

response:
{    
	"Result": [["SampleName","UniqueId"]],
    "StatusFlag": "<Status:1 if atleast 1 id exists, 0 if no id exista, -1 for input error>",
    "StatusCode": "[SUCCESS, FAIL, MISSING_SUBSRIPTION_KEY, MISSING_SAMPLE_IMAGE, INVALID_SUBSRIPTION_KEY, INVALID_USER, INVALID_GALLERY, INVALID_ID_NAME, FACE_NOT_STRAIGHT]",
    "StatusMessage": "<a message desccription>",
	"Version": "version number",
	"TTE": "time to execute in seconds"
}