import requests
import urllib
import json
import string
import sys
import re
import nltk
import csv
from nltk.corpus import cmudict
#def starts_with_vowel_sound(word, pronunciations=cmudict.dict()):
pronunciations = cmudict.dict()
def sounds_like_a_vowel(word):
	for syllables in pronunciations.get('word', []):
		return(syllables[0][-1].isdigit())

result = string.punctuation

result = result.replace(' ', '')
punctuation_list = []
for i in range(len(result)):
    punctuation_list.append(result[i])
vowels = ['a','e','i','o','u'];

input_file = sys.argv[1];
f = open(input_file);

word_string = f.read()

word_list = nltk.word_tokenize(word_string);
correction = {}
article_list = {"a","an","the"}
#print(word_list[:10])

#for i in range(len(word_list)):
#	word = word_list[i]
#	if(word not in punctuation_list and not in article-list):
#		if(word[0] in vowels or sounds_like_a_vowel(word)):
#			if(word_list[i-1] not in punctuation_list and word_list[i-1]=='an'):
#				continue;
#			elif(word_list[i-1] not in punctuation_list):
#				print_error(word_list[i-1],)

for i in range(len(word_list)):
	word = word_list[i];
	if(word in article_list):
		word_bef = word_list[i-1]
		word_after = word_list[i+1]
		b1 = "https://api.phrasefinder.io/search?corpus=eng-us&query=" + urllib.parse.quote(word_bef + " " + "a" + " " + word_after) + "&format=tsv"
		b2 = "https://api.phrasefinder.io/search?corpus=eng-us&query=" + urllib.parse.quote(word_bef + " " + "an" + " " + word_after) + "&format=tsv"
		b3 = "https://api.phrasefinder.io/search?corpus=eng-us&query=" + urllib.parse.quote(word_bef + " " + "the" + " " + word_after) + "&format=tsv"
		        #	print("Search ended")
		phrasefinder = requests.get(b1)
		ans = phrasefinder.text
		val1 = 0
		if len(ans)>0:
		    for row in ans.split('\n'):
		        if len(row) > 0:
		        	spl = row.split()
		        	val1 += int(spl[len(spl)-6])

		
		phrasefinder = requests.get(b2)
		ans = phrasefinder.text
		val2 = 0
		if len(ans)>0:
		    for row in ans.split('\n'):
		        if len(row) > 0:
		        	spl = row.split()
		        	val2 += int(spl[len(spl)-6])

		phrasefinder = requests.get(b3)
		ans = phrasefinder.text
		val3 = 0
		if len(ans)>0:
		    for row in ans.split('\n'):
		        if len(row) > 0:
		        	spl = row.split()
		        	val3 += int(spl[len(spl)-6])        	


		if(val1 == max(val1,max(val2,val3))):
			if(word == "a"):
				continue
			else:
				correction[i+1] = "a"
		elif(val2 == max(val1,max(val2,val3))):
			if(word == "an"):
				continue
			else:
				correction[i+1] = "an"
		else:
			if(word == "the"):
				continue
			else:
				correction[i+1] = "the"


for k,v in correction.items():
	print("Correction in word no. {} is {}. ".format(k,v))




