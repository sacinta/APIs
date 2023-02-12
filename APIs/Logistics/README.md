# API Structure for Logistics

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
1. Get Locations - Gub HUB locations added from Admin srction
2. Asset Scan - Scan Asset QR/Bar code
3. Send Live Tracking - Send live tracking data
4. Save Asset Location - Save new asset location
5. Current Asset Status - Get current asset status report
6. Current Location Status - Get list of all active and inactive locations and assets present in them
7. Schedule Asset Scan Log - Schedule a report for the asset scan log
8. Schedule Live Tracking Log - Schedule a report for the live tracking log
9. Audit Survey Form - Download the current audit survey form
10. Manage Assets - Manage assets to add/remove from repository

## Get Locations
This function returns the **hub locations**. To add more hub locations, please go to [Manage Locations Page](http://127.0.0.1:5000/logistics/admin/manage-locations)

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/asset:get_locations**

The only input needed for this function is the API key. If the user is part of an *Orgnaization*, it returns all the hub locations available in the organization

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |

Example JSON:

    {
	    "ApiKey": "api key string"
    }

#### Receive JSON
If successful, the result contains the hub details in the result. 

| Result Field | Description |
| --- | --- |
| `Locations` | List of location dictionaries - {id, name, latitude, longitude} |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| Locations Field | Description |
| --- | --- |
| `Locations` | List of locations |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Locations obtained successfully |
| `FAIL_NO_LOCATIONS` | 0 | No locations added. Please add locations using web service |
| `FAIL_GET_LOCATIONS` | 0 | Unable to get locations |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

Example JSON: *User Langauge is German* 

    {
	    "ApiCode": "ACTIVE",
	    "ApiFlag": 1,
	    "ApiMessage": "API ist aktiv",
	    "ResponseCode": "SUCCESS",
	    "ResponseFlag": 1,
	    "ResponseMessage": "Erfolgreich gewonnene Standorte",
	    "Result": {
		   "Locations": [
		       {
		           "LocationCode": null,
		           "LocationId": 7,
		           "LocationIsActive": false,
		           "LocationLat": "52.51622086393074",
		           "LocationLong": "13.417327855713669",
		           "LocationName": "Berlin"
		       },
		       {
		           "LocationCode": null,
		           "LocationId": 4,
		           "LocationIsActive": false,
		           "LocationLat": "13.082153590400935",
		           "LocationLong": "80.28012082446367",
		           "LocationName": "Chennai"
		       }
	      ],
	      "ResultCode": "SUCCESS",
	      "ResultFlag": 1,
	      "ResultMessage": "Erfolgreich gewonnene Standorte"
	     } 
		"TTE": '0.01s'
	}
									  
## Asset Scan
This function is used to scan the asset QR/Bar code

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/asset:scan**

| Field | Type | Description |
| --- | --- | --- |
| `AssetImage` | *Either AssetImage of the AssetCode Required* | Base64 Encoded image of the QR/Bar Code.|
| `AssetCode` | *Either AssetImage of the AssetCode Required* | Asset code string. *Either AssetImage of the AssetCode must be supplied* |
| `ScanType` | Required | can be **Drop** or **Pick** |
| `ScanTimeUTC` | Required | Scan time in UTC format. *This input is optional* |
| `LocationId` | Required | Location ID of the hub. Get this from *asset:get_locations()* function. |
| `LocationLat` | Optional | Location latitude value |
| `LocationLong` | Optional | Location longitude value |
| `LocationDistance` | Optional | Current scan location distance from the selected hub |

| Asset Field | Description |
| --- | --- |
| Sample Number | Input Field 1 |
Sample number can be any unique alphanumeric string.

The final JSON. 
										   
| Field | Description |
| --- | --- | --- |
| `ApiKey` | User API Key |
| `Asset` | Asset Field |

Example JSON:

    {
	    "ApiKey": "api key string", 
	    "Asset":{
		    "101145":{
			    "AssetCode":"036000291452",
			    "ScanType":"Drop", 
			    "LocationId":8, 
			    "LocationLat":"135.256",
			    "LocationLong":"-256.135",
			    "ScanTimeUTC":"2022-02-09 10:11:45.2"
		    }, 									  
		    "101215":{
			    "AssetImage":"base64 encoded string", 
			    "ScanType":"Pick", 
			    "LocationId":8, 
			    "LocationLat":"135.256", 
			    "LocationLong":"-256.135", 
			    "ScanTimeUTC":"2022-02-09 10:12:15.5"
		    }
	    }
    }
									  
#### Receive JSON
If successful, the result contains the scan info for each sample.  The response will contain results for each of the sample numbers.

| Result Field | Description |
| --- | --- |
| `Drops` | Total drops for today |
| `Picks` | Total picks for today |
| `ScanResults` | List of scan result dictionaries |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |


| ScanResults Field | Description |
| --- | --- |
| `SampleNumber` | Scan result for sample number |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |


| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Locations obtained successfully |
| `FAIL_INVALID_INPUTS` | 0 | Invalid inputs for all samples |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |


| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Scan(s) successful |
| `FAIL_ASSET_NOT_IN_INVENROTY` | 0 | Asset not in inventory |
| `FAIL_SCAN` | 0 | Scan(s) failed |
| `INVALID_LOCATION_ID` | 0 | Location invalid |
| `MISSING_ASSET_INFO` | -1 | No asset image or code supplied |

Example JSON: *User Langauge is German* 

    {
	    "ApiCode": "ACTIVE", 
	    "ApiFlag": 1, 
	    "ApiMessage": "API ist aktiv", 
	    "ResponseCode": "SUCCESS", 
	    "ResponseFlag": 1, "ResponseMessage": "2 scan(s) erfolgreich",  
	    "Result": {
		    "Drops": 1, 
		    "Picks": 1, 
		    "ResultCode": "SUCCESS", 
		    "ResultFlag": 1, 
		    "ResultMessage": "Scan(s) erfolgreich", 
		    "ScanResults": [
			   	{
				   "ResultCode": "SUCCESS", 
				   "ResultFlag": 1, 
				   "ResultMessage": "Scan(s) erfolgreich", 
				   "SampleNumber": "101145"
			   	}, 
			   	{"
				   "ResultCode": "SUCCESS", 
				   "ResultFlag": 1, 
				   "ResultMessage": "Scan(s) erfolgreich", 
				   "SampleNumber": "101215"
			   	}
		  	]
	   	}, 
	   	"TTE": "0.60s"
   	} 
	
##  Send Live Tracking
This function is used to send live tracking data	
### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/track:send_live_tracking**

| Input Field | Type | Description |
| --- | --- | --- |
| `RouteUUID` | Required | UUID for the current route |
| `LocationLat` | Required | Location latitude value |
| `LocationLong` | Required | Location longitude value |
| `LogTimeUTC` | Requried | Log time in UTC format |
| `LocationAccuracy` | Optional | Location accuracy in meters |
| `Speed` | Optional | Speed in kmph |
| `Altitude` | Optional | Altitude in meters |
| `AltitudeAccuracy` | Optional | Altitude accuracy in meters |

| LocationData Field | Description |
| --- | --- |
| Sample Number | Input Field 1 |

The final JSON. 
										   
| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required |User API Key |
| `LocationData` | Required | Location Data Field |

Example JSON:

    {
	    "LocationData": {
		    "data1": {
		        "RouteUUID": "123456",
		        "LocationLat": 17,
		        "LocationLong": 16,
		        "LogTimeUTC": "2023-01-26 09:10:00",
		        "LocationAccuracy": 10,
		        "Speed": 10,
		        "Altitude": 10,
		        "AltitudeAccuracy": 10
		    }
	    },
	    "ApiKey": "api key string"
    }
									  
#### Receive JSON
If successful, the result contains the status for the live location samples. The response will contain results for each of the sample numbers.

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Result for SampleNumber |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Live tracking updated successfully |
| `FAIL_INVALID_INPUTS` | 0 | Invalid inputs for all samples |
| `MISSING_LOCATION_DATA` | -1 | Location data missing |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Live tracking updated successfully |
| `FAIL_INVALID_INPUTS` | 0 | Invalid inputs for all samples |
| `MISSING_LOG_TIME_UTC` | -1 | Missing log time in UTC |
| `MISSING_LOCATION_DATA` | -1 | Location data missing |
`FORMATTING_ERROR` | -1 | Please check the JSON format and try again |

Example JSON: *User Langauge is English* 

    {
        "ApiCode": "ACTIVE",
        "ApiFlag": 1,
        "ApiMessage": "API is active",
        "ResponseCode": "SUCCESS",
        "ResponseFlag": 1,
        "ResponseMessage": "1/1 Locations obtained successfully",
        "Result": [
            {
                "ResultCode": "SUCCESS",
                "ResultFlag": 1,
                "ResultMessage": "Live tracking updated successfully",
                "SampleNumber": "data1"
            }
        ],
        "TTE": "0.85s"
    }

##  Save Asset Locations
This function is used to create or update an assset location
### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/admin:asset:save_locations**

| Input Field | Type | Description |
| --- | --- | --- |
| `LocationCode` | Required | Location code |
| `LocationName` | Requried | Locatio name |
| `LocationLat` | Required | Location latitude value |
| `LocationLong` | Required | Location longitude value |
| `LocationId` | Optional | Existing Location ID. If provided, update code, name, lat, long and active values from here. A new location is created if the id is absent |
| `LocationIsActive` | Optional | **True** or **False** |

For each of the inputs, create the asset filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.
| Locations Field | Description |
| --- | --- |
| Sample Number | Input Field 1 |

The final JSON. 
										   
| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required |User API Key |
| `Locations` | Required | Locations List Field |

Example JSON:

    {
        "Locations": [
            {
                "LocationCode": "HYD-WM2",
                "LocationName": "WM2",
                "LocationLat": 17.4,
                "LocationLong": 78.5,
                "LocationIsActive": true
            }
        ],
        "ApiKey": "api key string"
    }
									  
#### Receive JSON
If successful, the result contains the status regarding new location. The response will contain results for each of the sample numbers.

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Result for SampleNumber |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Locations saved successfully |
| `SUCCESS` | 1 | *success-samples/total-samples* Locations saved successfully |
| `FAIL_INVALID_INPUTS` | 0 | Invalid inputs for all samples |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |
| `INVALID_PERMISSION` | -1 | This API requires Admin Permission, please contact your admin |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Location saved successfully |
| `FAIL_INVALID_INPUT` | 0 | Invalid inputs for all samples |
| `FAIL_INVALID_INPUTS` | 0 | Invalid inputs for all samples |
| `MISSING_LOCATION_CODE` | 0 | Invalid inputs for all samples |
| `MISSING_LOCATION_NAME` | -1 | Missing log time in UTC |
| `MISSING_LOCATION` | -1 | Location data missing |
| `MISSING_LOCATION_ACTIVE_STATUS` | -1 | Location data missing |
| `INVALID_LOCATION_ACTIVE_STATUS` | -1 | Location data missing |
`FORMATTING_ERROR` | -1 | Please check the JSON format and try again |

Example JSON: *User Langauge is English* 

    {
        "ApiCode": "ACTIVE",
        "ApiFlag": 1,
        "ApiMessage": "API is active",
        "ResponseCode": "SUCCESS",
        "ResponseFlag": 1,
        "ResponseMessage": "1/1 Locations saved successfully",
        "Result": [
            {
                "ResultCode": "LOCATIONS_SAVED",
                "ResultFlag": 1,
                "ResultMessage": "Location saved successfully",
                "SampleNumber": 1
            }
        ],
        "TTE": "0.27s"
    }
	
## Current Asset Status
This function is used to get the current asset status

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/report:asset:current_status**

The only input needed for this function is the API key.
| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
				
Example JSON:

    {
	    "ApiKey": "api key string"
    }
				
#### Receive JSON
If successful, the result contains the current asset status

| Result Field | Description |
| --- | --- |
| `Status` | List of current assets|
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

 Status Field | Description |
| --- | --- |
| `AdminEmail` | Admin email linked with asset|
| `AdminID` | Admin id linked with asset |
| `AdminName` | Admin name linked with asset |
| `AssetCode` | Asset code linked with asset |
| `DeviceID` | Device id used in scanning asset |
| `DeviceName` | Device name used in scanning asset |
| `DeviceUniqueID` | Device unique id used in scanning asset |
| `LocationName` | Location name where was the asset was scanned|
| `LocationId` | Location id where was the asset was scanned|
| `LocationIsActive` | Location status where was the asset was scanned|
| `LocationLat` | Latitude of the location |
| `LocationLong` | Longitude of the location |
| `LogCreatedAtUTC` | Asset log created time in UTC format |
| `LogID` | Log ID |
| `ScanType` | **Drop** or **Pick** |
| `Survey` | Survey attached with the asset |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Status retrieved successfully |
| `FAIL_NO_DATA` | 0 | No data available |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

Example JSON: *User Langauge is English* 

    {
        "ApiCode": "ACTIVE",
        "ApiFlag": 1,
        "ApiMessage": "API is active",
        "ResponseCode": "SUCCESS",
        "ResponseFlag": 1,
        "ResponseMessage": "Status retrieved successfully",
        "Result": {
            "ResultCode": "SUCCESS",
            "ResultFlag": 1,
            "ResultMessage": "Status retrieved successfully",
            "Status": [
                {
                    "AdminEmail": "admin@email.com",
                    "AdminID": 100,
                    "AdminName": "admin name",
                    "AssetCode": "1628490567",
                    "DeviceID": "None",
                    "DeviceName": "None",
                    "DeviceUniqueID": "None",
                    "LocationCode": "HYD-WM2",
                    "LocationId": 8,
                    "LocationIsActive": true,
                    "LocationLat": "17.4",
                    "LocationLong": "78.5",
                    "LocationName": "WM2",
                    "LogCreatedAtUTC": "Mon, 09 Aug 2021 11:59:28 GMT",
                    "LogID": 10,
                    "ScanType": "Drop",
                    "Survey": "None"
                }
             ]
         }
         "TTE": "0.23s"
	}

## Current Location Status
This function is used to get the current location status

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/report:asset:current_location_status**

The only input needed for this function is the API key.
| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
				
Example JSON:

    {
	    "ApiKey": "api key string"
    }
				
#### Receive JSON
If successful, the result contains the current location status

| Result Field | Description |
| --- | --- |
| `Status` | List of current assets|
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

 Status Field | Description |
| --- | --- |
| `AssetCount` | Admin email linked with asset|
| `LocationCode` | Admin id linked with asset |
| `LocationId` | Location id where was the asset was scanned|
| `LocationIsActive` | Location status where was the asset was scanned|
| `LocationName` | Location name where was the asset was scanned|
| `LocationLat` | Latitude of the location |
| `LocationLong` | Longitude of the location |
| `LogCreatedAtUTC` | Asset log created time in UTC format |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Status retrieved successfully |
| `FAIL_NO_DATA` | 0 | No data available |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

Example JSON: *User Langauge is English* 

    {
	    "ApiCode": "ACTIVE",
	    "ApiFlag": 1,
	    "ApiMessage": "API is active",
	    "ResponseCode": "SUCCESS",
	    "ResponseFlag": 1,
	    "ResponseMessage": "Status retrieved successfully",
	    "Result": {
	        "ResultCode": "SUCCESS",
	        "ResultFlag": 1,
	        "ResultMessage": "Status retrieved successfully",
	        "Status": [
	            {
	                "AssetCount": 0,
	                "LocationCode": "HYD-WM2",
	                "LocationId": 8,
	                "LocationIsActive": true,
	                "LocationLat": "17.4",
	                "LocationLong": "78.5",
	                "LocationName": WM2"
	            }
             ]
         }
         "TTE": "0.23s"
	}

##  Schedule Asset Scan Log
This function is used to schedule a report for the asset scan log
### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/report:schedule:asset_scan_log**

Request JSON. 
										   
| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required |User API Key |
| `StartDate` | Required | Log start date |
| `EndDate` | Required | Log end date |

Example JSON:

    {
        "StartDate": "2023-01-01",
        "EndDate": "2023-01-20",
        "ApiKey": "api string key"
    }
									  
#### Receive JSON
If successful, the result contains the asset scan log

| Result Field | Description |
| --- | --- |
| `ReportManifest` | Report manifest details|
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

 ReportManifest Field | Description |
| --- | --- |
| `DownloadURL` | Download URL if available |
| `ExpiresAt` | Download expiration date |
| `ReportUUID` | Report UUID to download *from Reports API download_scheduled_report route*|
| `WaitMinutes` | Estimated wait time in minutes to download report|

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Report request scheduled successfully |
| `INVALID_DATE_UTC` | 1 | Invalid date |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Report request scheduled successfully |

Example JSON: *User Langauge is English* 

    {
	    "ApiCode": "ACTIVE",
	    "ApiFlag": 1,
	    "ApiMessage": "API is active",
	    "ResponseCode": "SUCCESS",
	    "ResponseFlag": 1,
	    "ResponseMessage": "Report request scheduled successfully",
	    "Result": {
	        "ReportManifest": {
	            "DownloadURL": "",
	            "ExpiresAt": "2023-01-27T13:03:47Z",
	            "ReportUUID": "ed357e63uuiduuid800824b9c21c5bb5",
	            "WaitMinutes": "2"
	        },
	        "ResultCode": "SUCCESS",
	        "ResultFlag": 1,
	        "ResultMessage": "Report request scheduled successfully"
	    },
	    "TTE": "0.29s"
	}

##  Schedule Live Track Log
This function is used to schedule a report for the live track log
### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/report:schedule:live_tracking_log**

Request JSON. 
										   
| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required |User API Key |
| `StartDate` | Required | Log start date |
| `EndDate` | Required | Log end date |

Example JSON:

    {
        "StartDate": "2023-01-01",
        "EndDate": "2023-01-20",
        "ApiKey": "api string key"
    }
									  
#### Receive JSON

If successful, the result contains the report manifest details

| Result Field | Description |
| --- | --- |
| `ReportManifest` | Report manifest details|
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

 ReportManifest Field | Description |
| --- | --- |
| `DownloadURL` | Download URL if available |
| `ExpiresAt` | Download expiration date |
| `ReportUUID` | Report UUID to download *from Reports API download_scheduled_report route*|
| `WaitMinutes` | Estimated wait time in minutes to download report|

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Report request scheduled successfully |
| `INVALID_DATE_UTC` | 1 | Invalid date |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Report request scheduled successfully |

Example JSON: *User Langauge is English* 

    {
	    "ApiCode": "ACTIVE",
	    "ApiFlag": 1,
	    "ApiMessage": "API is active",
	    "ResponseCode": "SUCCESS",
	    "ResponseFlag": 1,
	    "ResponseMessage": "Report request scheduled successfully",
	    "Result": {
	        "ReportManifest": {
	            "DownloadURL": "",
	            "ExpiresAt": "2023-01-27T13:09:21Z",
	            "ReportUUID": "e3c5d2a88eac4a1c88ce83c584798799",
	            "WaitMinutes": "2"
	        },
	        "ResultCode": "SUCCESS",
	        "ResultFlag": 1,
	        "ResultMessage": "Report request scheduled successfully"
	    },
	    "TTE": "0.35s"
	}
 
##  Audit Survey Forms
This function is used to schedule get the audit survey form
### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/audit:get_survey_forms**

Request JSON. 
										   
| Field | Type | Description |
| --- | --- | --- |
| `ApiKey` | Required |User API Key |

Example JSON:

    {
        "ApiKey": "api string key"
    }
									  
#### Receive JSON
If successful, the result contains the audit survey form.

| Result Field | Description |
| --- | --- |
| `Forms` | List of forms|
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

 Forms Field | Description |
| --- | --- |
| `AdminID` | Admin Id linked to the survey form |
| `SurveyForm` | Survey form |
| `SurveyID` | Survey Id|
| `SurveyIsActive` | Survey active status|

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Forms retrieved successfully |
| `INVALID_DATE_UTC` | 1 | Invalid date |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |


Example JSON: *User Langauge is English* 

    {
    "ApiCode": "ACTIVE",
    "ApiFlag": 1,
    "ApiMessage": "API is active",
    "ResponseCode": "SUCCESS",
    "ResponseFlag": 1,
    "ResponseMessage": "Forms retrieved successfully",
    "Result": {
        "Forms": [
            {
                "AdminID": 1,
                "SurveyForm": "[{\"Name\":\"name\",\"Label\":\"Name/Personnel ID\",\"Hint\":\"Enter Name/Personnel ID here\",\"Type\":\"text\"}]",
                "SurveyID": 1,
                "SurveyIsActive": true
            }
        ],
        "ResultCode": "SUCCESS",
        "ResultFlag": 1,
        "ResultMessage": "Forms retrieved successfully"
    },
    "TTE": "0.04s"
     	
## Manage Assets
Manage assets to add/remove from repository

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/admin:asset:manage**

Create an input for all the qr code or the base64 images that need to be scanned
| Input Field | Description |
| --- | --- |
| `AssetImage` | Base64 Encoded image of the QR/Bar Code. *Either AssetImage of the AssetCode must be supplied* |
| `AssetCode` | Asset code string. *Either AssetImage of the AssetCode must be supplied* |
| `AssetAction` | can be **Add** or **Drop** |

For each of the inputs, create the asset filed. Sample number can be any unique alphanumeric string. The response will contain results for each of the sample numbers.
| Asset Field | Description |
| --- | --- |
| Sample Number 1 | Input Field 1 |
| Sample Number 2 | Input Field 2 |

The final JSON. 
										   
| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
| `Asset` | Asset Field |

Example JSON:

{"ApiKey": "api key string", "Asset":{"101145":{"AssetCode":"036000291452", "AssetAction":"Add"},
									  "101215":{"AssetImage":"base64 encoded string", "AssetAction":"Add"}}}
									  
#### Receive JSON
If successful, the result contains the scan info for each sample

| Result Field | Description |
| --- | --- |
| `SampleNumber` | Scan result for sample number |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | <successfulCount>/<total> Scan(s) successful |
| `INVALID_ASSET` | 0 | Invalid inputs for all samples |
| `FAIL_INVALID_INPUTS` | 0 | Invalid inputs for all samples |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Asset added to inventory |
| `SUCCESS` | 1 | Asset already in inventory |
| `SUCCESS` | 1 | Asset does not exist |
| `SUCCESS` | 1 | Asset removed from inventory |
| `FAIL_ASSET_NOT_IN_INVENROTY` | 0 | Asset not in inventory |
| `FAIL_SCAN` | 0 | Scan(s) failed |
| `INVALID_LOCATION_ID` | 0 | Location invalid |
| `MISSING_ASSET_INFO` | -1 | No asset image or code supplied |
| `FORMATTING_ERROR` | -1 | Please check the JSON format and try again |
| `INVALID_ASSET_ACTION` | -1 | Invalid asset action |

Example JSON: *User Langauge is German* 

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '2/2 Scan(s) erfolgreich', 
'Result': [{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Asset bereits im Bestand', 'SampleNumber': '101145'}, 
		   {'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Asset bereits im Bestand', 'SampleNumber': '101215'}], 'TTE': '0.12s'}