import requests
import urllib
import json
import string
import sys
import re
import nltk
import csv
from nltk.corpus import cmudict

def frequency_finder(s1,s2,s3):
	b1 = "https://api.phrasefinder.io/search?corpus=eng-us&query=" + urllib.parse.quote(s1 + " " + s2 + " " + s3) + "&format=tsv"
	phrasefinder = requests.get(b1)
	ans = phrasefinder.text
	val1 = 0
	if len(ans)>0:
	    for row in ans.split('\n'):
	        if len(row) > 0:
	        	spl = row.split()
	        	val1 += int(spl[len(spl)-6])

	return val1
