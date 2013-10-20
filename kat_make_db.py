#!/usr/bin/env python
import urllib2
import datetime
req = urllib2.Request('http://www.kat.mvr.bg/statistik.asp')
response = urllib2.urlopen(req)
the_page = response.read()
#print the_page.decode("windows-1251")

from firebase import firebase
firebase = firebase.FirebaseApplication('https://kat.firebaseio.com', None)
now = datetime.datetime.now()
current_date = str(now.year) + " : " + str(now.month) + " : " + str(now.day)
result = firebase.post(current_date, the_page.decode("windows-1251"))
print result