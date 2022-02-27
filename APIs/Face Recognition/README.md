# API Structure for Face Recognition
This document contains the JSON structure to access the Face Recognition APIs. The *Receive JSONs* follow the main structure, to see, please check the readme in *[Main API](https://github.com/sacinta/sacinta-services/tree/main/APIs)*

**Updated 26-Feb-2022**
The following functions are available
1. Detect - Detects faces and returns bounding boxes for each face
2. Enroll - Enrolls a face
3. Recognize - Recognize faces in the given image and return the sample name and unique id for each associated face
4. Get Enrolls - Get the list of enrolled sample names and unqiue ids
5. Remove Enrolls - Remove ids from the database				
## Detect
This function returns the list of detected faces

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/detect**

Create the images filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.

| Images Field | Description |
| --- | --- |
| Sample Number 1 | Base64 Encoded image of the face(s) |
| Sample Number 2 | Base64 Encoded image of the face(s) |

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
| `SampleImages` | Images |

Example JSON:
{"ApiKey": "api key string", "SampleImages":{"1":"base64 encoded string",
											 "2":"base64 encoded string"}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result. 

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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '2 Gesicht(e) gefunden in 2 Bild(e)', 
	'Result': [{'BoundingBox': [56.0, 23.0, 100.0, 121.0], 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht erkannt', 'SampleNumber': '1'}, 
			   {'BoundingBox': [56.0, 23.0, 100.0, 121.0], 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht erkannt', 'SampleNumber': '2'}], 'TTE': '0.18s'}

## Enroll
This function is used to enroll faces

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/enroll**

Create the images filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.

*Note: Each image must contain only one face. Images with multiple faces will be rejected*

| Images Field | Description |
| --- | --- |
| Sample Number 1 | Base64 Encoded image of the face |
| Sample Number 2 | Base64 Encoded image of the face |

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
| `SampleImages` | Images |
| `UniqueId` | Unique id for the sample. Can be alphanumeric and -_ and space  |
| `SampleName` | Sample name. Can be alphanumeric and -_ and space |
| `SampleProfileImg` | Base64 Encoded profile thumbnail image of the sample. Face must be atleast 100x100 px |

Example JSON:

{'ApiKey': 'api key string', 'UniqueId': 't220226-01', 'SampleName': 'test', 'SampleProfileImg': 'dummy', 'SampleImages': {'1': 'base64 encoded string', '2': 'base64 encoded string'}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result. 

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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': 'Eingeschrieben 2/2 Bild(e)', 
	'Result': [{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht eingeschrieben', 'SampleNumber': '1'}, 
			   {'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht eingeschrieben', 'SampleNumber': '2'}], 'TTE': '0.6s'}
		
## Recognize
This function is used to recognize faces in the given image and return the sample name and unique id for each associated face

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/recognize**

Create the images filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.

| Images Field | Description |
| --- | --- |
| Sample Number 1 | Base64 Encoded image of the face(s) |
| Sample Number 2 | Base64 Encoded image of the face(s) |

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
| `SampleImages` | Images |
| `GalleryUniqueId` | Unique ID for the gallery (*Optional*). To add faces to gallery, please go to https://www.sacinta.com/face/map_gal_enroll |


Example JSON:

{"ApiKey": "api key string", "SampleImages":{"1":"base64 encoded string",
											 "2":"base64 encoded string"}}
									  
#### Receive JSON
If successful, the result contains the hub details in the result. 

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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '1 Gesicht(e) gefunden', 
	'Result': [{'BoundingBox': [51.0, 23.0, 105.0, 132.0], 'Confidence': 78.2, 'MatchCode': '0x4e635752', 'MatchedId': 't01', 'MatchedName': 'test', 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Gesicht erkannt', 'SampleNumber': '1'}], 'TTE': '0.56s'}
			   
## Get Enrolls
This function is used to get the list of enrolled sample names and unqiue ids

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/get_enrolls**

The only input needed for this function is the API key.

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |

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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '4Id(s) exists', 
	'Result': {'Ids': [{'SampleName': 'test', 'UniqueId': 't01'}, 
					   {'SampleName': 'test1', 'UniqueId': 't02'}, 
					   {'SampleName': 'test2', 'UniqueId': 't03'}, 
					   {'SampleName': 'test3', 'UniqueId': 't04'}], 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Id(s) exists', 'TotalIds': 4}, 'TTE': '0.02s'}

## Remove Enrolls
This function is used to remove ids from the database

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/face/v1/remove_enrolls"*

Create the images filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.

| Unique ID Field | Description |
| --- | --- |
| Sample Number 1 | Unique ID of the first sample to be remvoed |
| Sample Number 2 | Unique ID of the second sample to be removed |

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
| `UniqueIds` | Unique ID Field |

Example JSON:
{"ApiKey": "api key string", "SampleImages":{"1":"t01",
											 "2":"t02"}}
									  
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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '2 Id(s) removed', 
	'Result': [{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Id successfully deleted', 'SampleNumber': '1', 'SampleUniqueId': 't011'},
			   {'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Id successfully deleted', 'SampleNumber': '2', 'SampleUniqueId': 't02'}], 'TTE': '0.21s'}

