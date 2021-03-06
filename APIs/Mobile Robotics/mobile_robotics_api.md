# Mobile Robotics APIs
Python APIs for Mobile Robotics services

You can access two services using the python APIs
1. obstacle_detection - identify obstalces and traversable paths in the image 
2. obstale_avoidance_basic - identify the best paths that is able to avoid obstacles


# obstacle_detection
url: https://www.sacinta.com/mobilerobo/obstacle_detection
request:
{
    "SubscriptionKey": "<Subscription Key>",
    "SampleImages": {
        "1": "<SampleImage in base 64 format>",        
    }
}

response:
{	
	"Result": [["image_number","ImageBase64","StatusFlag","StatusCode","StatusMessage"]],
    "StatusFlag": "<Status:1 if atleast 1 face is detected, 0 if no face detected, -1 for input error>",
    "StatusCode": "[SUCCESS, FAIL, MISSING_SUBSRIPTION_KEY, MISSING_SAMPLE_IMAGE, INVALID_SUBSRIPTION_KEY, INVALID_USER]",
    "StatusMessage": "<a message description>",
	"Version": "version number",
	"TTE": "time to execute in seconds"
} 

# obstacle_avoidance_basic
url: https://www.sacinta.com/mobilerobo/obstacle_avoidance_basic
request:
{
    "SubscriptionKey": "<Subscription Key>",
    "SampleImages": {
        "1": "<SampleImage in base 64 format>",        
    }
}

response:
{	
	"Result": [["image_number","BestDirectionAngle",""MaxDistanceFactor","MaxPathWidthFactor","StatusFlag","StatusCode","StatusMessage"]],
    "StatusFlag": "<Status:1 if atleast 1 face is detected, 0 if no face detected, -1 for input error>",
    "StatusCode": "[SUCCESS, FAIL, MISSING_SUBSRIPTION_KEY, MISSING_SAMPLE_IMAGE, INVALID_SUBSRIPTION_KEY, INVALID_USER, MISSING_SAFE_DISTANCE_FACTOR, MISSING_MINIMUM_PATH_WIDTH_FACTOR, MISSING_MAXIMUM_OBJECT_HEIGHT_FACTOR, MISSING_MAXIMUM_OBJECT_WIDTH_FACTOR]",
    "StatusMessage": "<a message description>",
	"Version": "version number",
	"TTE": "time to execute in seconds"
} 