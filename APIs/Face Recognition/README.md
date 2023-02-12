
# API Structure for Face Recognition

## API Basic Template
This document contains the basic JSON structure to access the APIs. Please check each service to check the exact details.  You can try all the templates from [API Templates Page](https://www.sacinta.com/api-templates/api-key)

### Send JSON
The JSON structure for different versions are specific to the function. There are a few mandatory inputs for all the functions, and are as follows

### Version v1
**API Keys can be obtained from [API Templates Page](https://www.sacinta.com/api-templates/api-key)**
| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |

### Receive JSON
The JSON structure for different versions are as follows:
		
### Version v1
| Field | Description |
| --- | --- |
| `TTE` | Time to execute the function in seconds **seconds** |
| `ApiCode` | **OBSOLETE**, **DEPRECATED** or **ACTIVE** |
| `ApiFlag` | 1 for **ACTIVE** , 0 for **DEPRECATED**, -1 for **OBSOLETE**|
| `ApiMessage` | API message in user preferred language. Default is **English** |
| `ResponseCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResponseFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResponseMessage` | Response message in user preferred language. Default is **English** |
| `Result` | JSON Result for the specific function. *Result is only available if ResponseFlag is 0 or 1* |

| Result Field | Description |
| --- | --- |
| Keys Specific to each function | Results specific to function |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

1. *API Fields* contain info regarding the request api version
   - Response and the Result fields are only available if the API version is  **ACTIVE** or **DEPRECATED**
2. *Response Fields* contains info regarding the validity of the inputs. 
   - If the user has missed any of the mandatory inputs or if the user does not have the permission to access the service, it will return an error. 
   - If all the inputs are okay, it will return **SUCCESS**
3. *Result Fields* contain results for all the inputs.
   - It's possible to send multiple inputs to the service, the result field will contain the info regarding each input
   - Each input has the result keys specific to the function allong with *ResultCode* *ResultFlag* and the *ResultMessage*.
   
## API Functions Available
The following functions are available
1. Detect - Detects faces and returns bounding boxes for each face
2. Enroll - Enrolls a face
3. Recognize - Recognize faces in the given image and return the sample name and unique id for each associated face
4. Get Enrolls - Get the list of enrolled sample names and unqiue ids
5. Remove Enrolls - Remove ids from the database				
## Detect
This function returns the list of detected faces in all the sample images

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/detect**

| SampleImages Field |Description |
| --- | --- | --- |
| Sample Number | Base64 Encoded image of the face(s) |
Sample number can be any unique alphanumeric string.

| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required | User API Key |
| `SampleImages` | Required | Images |

Example JSON:
{"ApiKey": "api key string", "SampleImages":{"sample1":"base64 encoded string",  "sample2":"base64 encoded string"}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result. The response will contain results for each of the sample number.

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Result for sample number |
| `BoundingBox` | Bounding box of the face |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | <successCount> Face(s) found in <total> image(s)  |
| `FAIL_FACE_NOT_DETECTED` | 0 | Face not found |
| `MISSING_SAMPLE_IMAGE` | -1 | No sample image(s) supplied |
| `IMAGE_EXCEEDS_SIZE` | -1 | Sample image too big, maximum image size is 1.5MB |
| `EXCEPTION_FACE_DETECT` | -1 | Exception in face detect. If problem persists, contact us |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Face detected |
		
Example JSON: *User Langauge is German* 

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '2 Gesicht(e) gefunden in 2 Bild(e)', 'Result': [{'BoundingBox': [56.0, 23.0, 100.0, 121.0], 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht erkannt', 'SampleNumber': 'sample1'},  {'BoundingBox': [56.0, 23.0, 100.0, 121.0], 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht erkannt', 'SampleNumber': 'sample2'}], 'TTE': '0.18s'}

## Enroll
This function is used to enroll faces

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/enroll**

*Note: Each image must contain only one face. Images with multiple faces will be rejected*

| SampleImages Field | Description |
| --- | --- |
| Sample Number | Base64 Encoded image of the face |
Sample number can be any unique alphanumeric string. 

| Field | Type | Description |
| --- | --- | --- | 
| `ApiKey` | Mandatory | User API Key |
| `SampleImages` | Mandatory | Images |
| `UniqueId` | Mandatory | Unique id for the sample. Can be alphanumeric and -_ and space  |
| `SampleName` | Mandatory | Sample name. Can be alphanumeric and -_ and space |
| `SampleProfileImg` | Optional | Base64 Encoded profile thumbnail image of the sample. Face must be atleast 100x100 px |

Example JSON:

{'ApiKey': 'api key string', 'UniqueId': 't220226-01', 'SampleName': 'test', 'SampleProfileImg': 'dummy', 'SampleImages': {'sample1': 'base64 encoded string', 'sample2': 'base64 encoded string'}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result.  The response will contain results for each of the sample number.

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Result for sample number |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |
												
| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Enrolled <successCount>/<total> image(s)  |
| `FAIL_FACE_ERROR` | 0 | No face detected |
| `MISSING_SAMPLE_IMAGE` | -1 | No sample image(s) supplied |
| `IMAGE_EXCEEDS_SIZE` | -1 | Sample image too big, maximum image size is 1.5MB |
| `MISSING_PROFILE_IMAGE` | -1 | No profile image supplied |
| `PROFILE_IMAGE_EXCEEDS_SIZE` | -1 | Profile image too big, maximum image size is 1.5MB |
| `MISSING_SAMPLE_NAME` | -1 | Enrollment name missing |
| `INVALID_SAMPLE_NAME` | -1 | Enrollment name cannot contain special characters |
| `MISSING_UNIQUE_ID` | -1 | Unique id missing |
| `INVALID_UNIQUE_ID` | -1 | Unique id cannot contain special characters |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Face enrolled |
| `FAIL_MULTIPLE_FACES_DETECTED` | 0 | Multiple faces detected. Enroll image must contain only one face |
| `FAIL_FACE_NOT_DETECTED` | 0 | Face not found |
| `FAIL_FACE_SIZE_SMALL` | 0 | Face size small |
		
Example JSON: *User Langauge is German* 

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': 'Eingeschrieben 2/2 Bild(e)', 	'Result': [{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht eingeschrieben', 'SampleNumber': 'sample1'}, {'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht eingeschrieben', 'SampleNumber': 'sample2'}], 'TTE': '0.6s'}
		
## Recognize
This function is used to recognize faces in the given image and return the sample name and unique id for each associated face

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/recognize**

| SampleImages Field | Description |
| --- | --- |
| Sample Number | Base64 Encoded image of the face(s) |
Sample number can be any unique alphanumeric string.

| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required | User API Key |
| `SampleImages` | Required | Images |
| `GalleryUniqueId` | Optional | Unique ID for the gallery . To add faces to gallery, please go to https://www.sacinta.com/face/manage-galleries/map-gal-enroll |


Example JSON:

{"ApiKey": "api key string", "SampleImages":{"sample1":"base64 encoded string"}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result.  The response will contain results for each of the sample numbers.

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Result for sample number |
| `BoundingBox` | Bounding box of the face |
| `Confidence` | Confidence % for recognition |
| `MatchCode` | Matching code for recognition |
| `MatchedId` | Unique ID of the matched face |
| `MatchedName` | Name of the matched face |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | <successCount> Face(s) found  |
| `EXCEPTION_FACE_DETECT` | -1 | Exception in face detect. If problem persists, contact us |
| `FAIL_GALLERY_EMPTY` | 0| Gallery is empty |
| `FAIL_DATABASE_EMPTY` | 0 | Database is empty |
| `FAIL_FACE_NOT_RECOGNIZED` | 0 | Face not recognized |
| `FAIL_FACE_NOT_DETECTED` | 0 | Face not found |
| `MISSING_SAMPLE_IMAGE` | -1 | No sample image(s) supplied |
| `IMAGE_EXCEEDS_SIZE` | -1 | Sample image too big, maximum image size is 1.5MB |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Face recognized |
| `FAIL_FACE_NOT_CLEAR` | 0 | Face not clear |
| `FAIL_FACE_NOT_RECOGNIZED` | 1 | Face not recognized |
| `FAIL_FACE_SIZE_SMALL` | 1 | Face size small |

		
Example JSON: *User Langauge is German* 

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '1 Gesicht(e) gefunden', 	'Result': [{'BoundingBox': [51.0, 23.0, 105.0, 132.0], 'Confidence': 78.2, 'MatchCode': '0x4e635752', 'MatchedId': 't01', 'MatchedName': 'test', 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht erkannt', 'SampleNumber': 'sample1'}], 'TTE': '0.56s'}
			   
## Get Enrolls
This function is used to get the list of enrolled sample names and unqiue ids

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/get_enrolls**

The only input needed for this function is the API key.

| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required | User API Key |

Example JSON:
{"ApiKey": "api key string"}
									  
#### Receive JSON
If successful, the result contains the hub details in the result. 

| Result Field | Description |
| --- | --- |
| `Ids` | List of sample names and unique Ids |
| `TotalIds` | Total number of Ids |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| Ids Field | Description |
| --- | --- |
| `SampleName` | Sample name |
| `UniqueId` | Sample Unique Id |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | <idsCount> Id(s) exists  |
| `FAIL_NO_IDS` | 0 | No ids available |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Id(s) exists |
		
Example JSON:

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '4Id(s) exists', 	'Result': {'Ids': [{'SampleName': 'test', 'UniqueId': 't01'}, {'SampleName': 'test1', 'UniqueId': 't02'}, 
{'SampleName': 'test2', 'UniqueId': 't03'}, {'SampleName': 'test3', 'UniqueId': 't04'}], 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Id(s) exists', 'TotalIds': 4}, 'TTE': '0.02s'}

## Remove Enrolls
This function is used to remove ids from the database

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/remove_enrolls"*

Create the images filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.

| Unique ID Field | TyDescription |
| --- | --- |
| Sample Number | Unique ID of the first sample to be remvoed |

| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required | User API Key |
| `UniqueIds` | Required | Unique ID Field |

Example JSON:
{"ApiKey": "api key string", "SampleImages":{"sample1":"t01", "sample2":"t02"}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result. 

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Result for sample number |
| `SampleUniqueId` | UniqueId of the sample |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | <successCount> Id(s) removed  |
| `FAIL_INVALID_UNIQUE_ID` | 0 | Invalid Unique Id |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Id successfully deleted |
| `FAIL_ID_DOES_NOT_EXIST` | 0 | Id does not exist |
		
Example JSON:

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '2 Id(s) removed', 	'Result': [{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Id successfully deleted', 'SampleNumber': 'sample1', 'SampleUniqueId': 't011'}, {'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Id successfully deleted', 'SampleNumber': 'sample2', 'SampleUniqueId': 't02'}], 'TTE': '0.21s'}