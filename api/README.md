# API Documentation

## 1) Purpose

## 2) Methods

## 3) Endpoints

### Test endpoints

#### [GET] /ping/<name>

This endpoint can be used to check connectivity to the API. The `<name>` field
creates a personalized response:

	{
		"status": 200,
		"info": "https://github.com/CS3398-Oberon-Fairies/CS3398-Oberon-F2018/api/",
		"hello": "<name>"
	}

Alternatively, a 404 status response would do the same thing. Your call...

### Search endpoints

#### [GET] /location/search/<latitude>,<longitude>?[radius=10]

This endpoint will return parking spots within a radius, calculated in relation
to a given `latitude` and `longitude`.

*Params:*
- radius => (in miles) default:10, max:50, min:1

#### [GET] /location/search/<query>?[radius=10]

This endpoint will return parking spots within a radius, calculated in relation
to a given search `query` (for example: University Drive, San Marcos, TX).

*Params:*
- radius => (in miles) default:10, max:50, min:1

### Report endpoints *Future implementations*

#### [PUT] /location/report/parking/<latitude>,<longitude>

Report that a parking spot is now taken, in a given `latitude` and `longitude`.

#### [PUT] /location/report/leaving/<latitude>,<longitude>

Report that a parking spot is now freeing up, in a given `latitude` and 
`longitude`.

#### [PUT] /location/report/full/<latitude>,<longitude>

Report that a parking lot is full, in a given `latitude` and `longitude`.
