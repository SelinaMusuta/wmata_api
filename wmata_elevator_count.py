#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by Selina Musuta - @pumzi_code
#
# Simple WMATA API script -- we want to find out 
# the number of elevators out of service on the Green Line
#
# Exception Handling
try:
	from urllib2 import urlopen, Request
except ImportError:
	from urllib.request import urlopen, Request

print(urlopen)