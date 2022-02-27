# API Structure for Logistics Manager
This document contains the JSON structure to access the Logistics Manage APIs. The *Receive JSONs* follow the main structure, to see, please check the readme in *[Main API](https://github.com/sacinta/sacinta-services/tree/main/APIs)*

**Updated 26-Feb-2022**
The following functions are available
1. Get Locations - Gub HUB locations added from Admin srction
2. Asset Scan - Scan Asset QR/Bar code
3. Asset Current Status - Get current asset status
4. Manage Assets - Manage assets to add/remove from repository

## Get Locations
This function returns the **hub locations**. To add more hub locations, please go to https://www.sacinta.com/logistics/admin

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/asset:get_locations**

The only input needed for this function is the API key. If the user is part of an *Orgnaization*, it returns all the hub locations available in the organization

| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |

Example JSON:

{"ApiKey": "api key string"}

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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': 'Standorte erfolgreich abgerufen', 
	'Result': {'Locations': [[8, 'Hub1', 52.44445276530211, 13.309069221887036], [11, 'Hub2', 52.54336304245326, 13.307111262756509], [9, 'Hub3', 52.53821063521657, 13.45430558529261]], 
	'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Standorte erfolgreich abgerufen'}, 'TTE': '0.01s'}
									  
## Asset Scan
This function is used to scan the asset QR/Bar code

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/asset:scan**

Create an input for all the qr code or the base64 images that need to be scanned
| Input Field | Description |
| --- | --- |
| `AssetImage` | Base64 Encoded image of the QR/Bar Code. *Either AssetImage of the AssetCode must be supplied* |
| `AssetCode` | Asset code string. *Either AssetImage of the AssetCode must be supplied* |
| `ScanType` | can be **Drop** or **Pick** |
| `ScanTimeUTC` | Scan time in UTC format. *This input is optional* |
| `LocationId` | Location ID of the hub. Get this from previous function. *This input is optional* |
| `LocationLat` | Location latitude value *This input is optional* |
| `LocationLong` | Location long value *This input is optional* |
| `LocationDistance` | Current scan location distance from the selected hub *This input is optional* |

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

{"ApiKey": "api key string", "Asset":{"101145":{"AssetCode":"036000291452", "ScanType":"Drop", "LocationId":8, "LocationLat":"135.256", "LocationLong":"-256.135", "ScanTimeUTC":"2022-02-09 10:11:45.2"},
									  "101215":{"AssetImage":"base64 encoded string", "ScanType":"Pick", "LocationId":8, "LocationLat":"135.256", "LocationLong":"-256.135", "ScanTimeUTC":"2022-02-09 10:12:15.5"}}}
									  
#### Receive JSON
If successful, the result contains the scan info for each sample

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

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': '2 scan(s) erfolgreich', 
	'Result': {'Drops': 1, 'Picks': 1, 'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Scan(s) erfolgreich', 
	'ScanResults': [{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Scan(s) erfolgreich', 'SampleNumber': '101145'}, 
	{'ResultCode': 'SUCCESS', 'ResultFlag': 1, 'ResultMessage': 'Scan(s) erfolgreich', 'SampleNumber': '101215'}]}, 'TTE': '0.60s'} 
	
##Asset Current Status
This function is used to get the current asset status

### Version v1

#### Send JSON
**Route : https://api.sacinta.com/logistics/v1/admin:asset:current_status**

The only input needed for this function is the API key.
| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |
				
Example JSON:

{"ApiKey": "api key string"}
				
#### Receive JSON
If successful, the result contains the scan info for each sample

| Result Field | Description |
| --- | --- |
| `LocationID` | Location ID |
| `LocationIsActive` | **True** or **False**to specify if location is active |
| `LocationName` | Location name |
| `AssetCode` | Asset code |
| `CreatedAtUTC` | Asset log created time in UTC format |
| `LocationLat` | Latitude of the location |
| `LocationLong` | Longitude of the location |
| `LogID` | Log ID |
| `ScanType` | **Drop** or **Pick** |
| `UserEmail` | Email of the user that scanned |
| `UserName` | Name of the user that scanned |
| `ResultCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `ResultFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `ResultMessage` | Result message in user preferred language. Default is **English** |

| ResponseCode | ResponseFlag | ResponseMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | status retrieved successfully |
| `LIMIT_EXCEEDED` | -1 | This subscription has exceeded its request quota |
| `NOT_ALLOWED` | -1 | This subscription does not have access to the requested service |

| ResultCode | ResultFlag | ResultMessage |
| --- | --- | --- |
| `SUCCESS` | 1 | Status retrieved successfully |

Example JSON: *User Langauge is German* 

{'ApiCode': 'ACTIVE', 'ApiFlag': 1, 'ApiMessage': 'API ist aktiv', 'ResponseCode': 'SUCCESS', 'ResponseFlag': 1, 'ResponseMessage': 'Status erfolgreich abgerufen', 
	'Result': [{'LocationID': 8, 'LocationIsActive': True, 'LocationName': 'Hub1', AssetCode': '036000291452', 'CreatedAtUTC': '2022-02-09 10:11:45.2', 'LocationLat': '135.256', 'LocationLong': '-256.135', 'LogID': 10, 'ScanType': 'Drop', 'UserEmail': 'email@gmail.com', 'UID': 20, 'UserName': 'name'}, 
			   {'LocationID': 8, 'LocationIsActive': True, 'LocationName': 'Hub1', AssetCode': '036000291452', 'CreatedAtUTC': '2022-02-09 10:12:15.5', 'LocationLat': '135.256', 'LocationLong': '-256.135', 'LogID': 12, 'ScanType': 'Pick', 'UserEmail': 'email@gmail.com', 'UID': 20, 'UserName': 'name'}], 'TTE': '0.07s'}

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