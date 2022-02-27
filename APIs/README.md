# API Structure
This document contains the basic JSON structure to access the APIs. Please check each service to check the exact details.

## Send JSON
The JSON structure for different versions are specific to the function. There are a few mandatory inputs for all the functions, and are as follows

## Version v1
**API Keys can be obtained from [Profile Page](https://www.sacinta.com/profile)**
| Field | Description |
| --- | --- |
| `ApiKey` | User API Key |

## Version v0 *(Will become obsolete from 28-Feb-2022)*
| Field | Description |
| --- | --- |
| `SubscriptionKey` | User API Key |

## Receive JSON
The JSON structure for different versions are as follows:
		
## Version v1
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

1. API Fields contain info regarding the request api version
   - Response and the Result fields are only available if the API version is ACTIVE or DEPRECATED
2. Response Fields contains info regarding the validity of the inputs. 
   - If the user has missed any of the mandatory inputs or if the user does not have the permission to access the service, it will return an error. 
   - If all the inputs are okay, it will return **SUCCESS**
3. Result Fields contain results for all the inputs.
   - It's possible to send multiple inputs to the service, the result field will contain the info regarding each input
   - Each input has the result keys specific to the function allong with *ResultCode* *ResultFlag* and the *ResultMessage*.   
   
## Version v0 *(Will become obsolete from 28-Feb-2022)*
v0 API
Version			: 	code version
StatusTte		: 	time to execute in seconds
StatusFlag		: 	-1 for error, 0 for fail, 1 for success. Result only if flag is 0 or 1
StatusCode		: 	SUCCESS, FAIL, 
StatusMessage	: 	response message
Result			: 	result specific to function
					StatusFlag		: -1 for error, 0 for fail, 1 for success
					StatusCode		: SUCCESS, FAIL
					StatusMessage	: response message
| Field | Description |
| --- | --- |
| `Version` | Requested API version |
| `TTE` | Time to execute the function in seconds **seconds** |
| `StatusCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `StatusFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `StatusMessage` | Response message |
| `Result` | JSON Result for the specific function. *Result is only available if StatusFlag is 0 or 1* |

| Result Field | Description |
| --- | --- |
| Keys Specific to each function | Results specific to function |
| `StatusCode` | **SUCCESS**, **FAIL** or errors specific to function |
| `StatusFlag` | 1 for **SUCCESS**, 0 for **FAIL**,  and -1 for errors |
| `StatusMessage` | Result message in user preferred language. Default is **English** |

1. Status Fields inside the Result contain results for all the inputs and the ones outside contains info regarding the validity of inputs. 
2. Result Fields contain results for all the inputs.
   - It's possible to send multiple inputs to the service, the result field will contain the info regarding each input
   - Each input has the result keys specific to the function allong with *ResultCode* *ResultFlag* and the *ResultMessage*.   
