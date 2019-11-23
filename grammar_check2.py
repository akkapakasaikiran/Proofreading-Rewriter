import requests
import urllib
import json
import string
import sys
import re
import nltk
import csv
from frequency_finder import frequency_finder2
from frequency_finder import frequency_finder1

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
	word = word_list[i].lower();
	print(word)
	if(word in article_list):
		word_bef = word_list[i-1]
		word_after = word_list[i+1]
		if(word in article_list):
			#print(word)
			#print(word_after)

			#print(sounds_like_a_vowel(word_after))
			if(sounds_like_a_vowel(word_after) or starts_with_vowel_sound(word_after)):
				#print(word_after)
				if(word_bef in punctuation_list):
					if(word == "an"):
						val1 = frequency_finder2("an",word_after)
						val2 = frequency_finder2("the",word_after)
						if(val1>1000):
							continue
						else:
							if(val1>=val2):
								continue
							else:
								correction[i] = "the " + word_after
					else:
						val1 = frequency_finder2("an",word_after)
						val2 = frequency_finder2("the",word_after)
						if(val1>=val2):
							correction[i] = "an " + word_after
						else:
							correction[i] = "the " + word_after
				else:
					if(word == "an"):
						val1 = frequency_finder1(word_bef,"an",word_after)
						val2 = frequency_finder1(word_bef,"the",word_after)
						if(val1>1000):
							continue
						else:
							if(val1>=val2):
								continue
							else:
								correction[i] = "the " + word_after
					else:
						val1 = frequency_finder1(word_bef,"an",word_after)
						val2 = frequency_finder1(word_bef,"the",word_after)
						if(val1>=val2):
							correction[i] = "an " + word_after
						else:
							correction[i] = "the " + word_after
						
			else:
				if(word_bef in punctuation_list):
					if(word == "an"):
						val1 = frequency_finder2("a",word_after)
						val2 = frequency_finder2("the",word_after)
						if(val1>1000):
							continue
						else:
							if(val1>=val2):
								continue
							else:
								correction[i] = "the " + word_after
					else:
						val1 = frequency_finder2("a",word_after)
						val2 = frequency_finder2("the",word_after)
						if(val1>=val2):
							correction[i] = "a " + word_after
						else:
							correction[i] = "the " + word_after
				else:
					if(word == "a"):
						val1 = frequency_finder1(word_bef,"a",word_after)
						val2 = frequency_finder1(word_bef,"the",word_after)
						if(val1>1000):
							continue
						else:
							if(val1>=val2):
								continue
							else:
								correction[i] = "the " + word_after
					else:
						val1 = frequency_finder1(word_bef,"a",word_after)
						val2 = frequency_finder1(word_bef,"the",word_after)
						if(val1>=val2):
							correction[i] = "a " + word_after
						else:
							correction[i] = "the " + word_after
						

for k,v in correction.items():
	print("Correction in word no. {} is {}. ".format(k,v))
