#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Selina Musuta - @pumzi_code
#
# Simple WMATA API script -- we want to find out 
# the number of elevators out of service on the Green Line
#
# Exception Handling

import httplib, urllib, base64, json

try:
	from urllib2 import urlopen, Request
except ImportError:
	from urllib.request import urlopen, Request

demo_api_key = "6b700f7ea9db408e9745c207da7ca827"

# We want a list of all Elevator Incidents
incidents_url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'

# Set a JSON object with key/value for api key

hdrs = {'api_key': demo_api_key}

incidents_request = Request(incidents_url, headers=hdrs)

result = urlopen(incidents_request)

raw_data = result.read()

data = json.loads(raw_data.decode('utf8'))

print(data)

#######################################################

#Example code from WMATA API
headers = {
    # Request headers
    'api_key': '6b700f7ea9db408e9745c207da7ca827',
}

params = urllib.urlencode({
    # Request parameters
    'Route': 'X2',
})

try:
    conn = httplib.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/Incidents.svc/json/BusIncidents?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################