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
	from urllib import urlencode 
except ImportError:
	from urllib.request import urlopen, Request
	from urllib.parse import urlencode

def get_wmata_info(url, params=None):
	demo_api_key = "6b700f7ea9db408e9745c207da7ca827"
	# Set a JSON object with key/value for api key
	hdrs = {'api_key': demo_api_key}
	if params != None:
		encoded_params = urlencode(params)
		url = url + "?" + encoded_params
	# We want a list of all Elevator Incidents
	request = Request(incidents_url, headers=hdrs)
	result = urlopen(request)
	raw_data = result.read()
	data = json.loads(raw_data.decode('utf8'))
	return data

incidents_url = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'
incidents_data = get_wmata_info(incidents_url)

list_of_incidents =incidents_data['ElevatorIncidents']
print (list_of_incidents[0])

state_list_url = "https://api.wmata.com/Rail.svc/json/jStations" #[?LineCode]"

#print(data)

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