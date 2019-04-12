#!/usr/bin/python
import urllib2, json

#razor_slice = "node"
#value = "1aFuswDXsZjHiLsMGFQGV9"
#url = "http://29.1.65.14:8026/razor/api/" + razor_slice + "/" + "value"
url = "http://29.1.65.14:8026/razor/api/node/1aFuswDXsZjHiLsMGFQGV9"
data = json.loads(urllib2.urlopen(url))

info = data["ip_address"]

print 'DECODED', info
