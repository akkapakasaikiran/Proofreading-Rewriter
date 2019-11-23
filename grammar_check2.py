import requests
import urllib
import json
import string
import sys
import re
import nltk
import csv
from nltk.corpus import cmudict
def starts_with_vowel_sound(word, pronunciations=cmudict.dict()):
    for syllables in pronunciations.get(word, []):
        return syllables[0][-1].isdigit()
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
#print(word_list)
correction = {}
article_list = {'a',"an"}
#print(starts_with_vowel_sound("anonymous"))
for i in range(len(word_list)):
	word = word_list[i];
	if(word in article_list):
		word_bef = word_list[i-1]
		word_after = word_list[i+1]
		if(word in article_list):
			#print(word)
			#print(word_after)
			#print(sounds_like_a_vowel(word_after))
			if(sounds_like_a_vowel(word_after) or starts_with_vowel_sound(word_after)):
				#print(word_after)
				if(word == "an"):
					continue
				else:
					correction[i] = "an " + word_after
			else:
				if(word == "a"):
					continue
				else:
					correction[i] = "a " + word_after

for k,v in correction.items():
	print("Correction in word no. {} is {}. ".format(k,v))
