# import requests
# import urllib
# import json
import string
from time import time
start_time = time()
import nltk
print(time()-start_time)
from frequency_finder import frequency_finder2
from frequency_finder import frequency_finder1
print(time()-start_time)
result = string.punctuation

print(time()-start_time)

result = result.replace(' ', '')
punctuation_list = []
for i in range(len(result)):
    punctuation_list.append(result[i])

print(time()-start_time)

from nltk.corpus import cmudict
def starts_with_vowel_sound(word, pronunciations=cmudict.dict()):
    for syllables in pronunciations.get(word, []):
        return syllables[0][-1].isdigit()
#def starts_with_vowel_sound(word, pronunciations=cmudict.dict()):
pronunciations = cmudict.dict()

print(time()-start_time)

def sounds_like_a_vowel(word):
	for syllables in pronunciations.get('word', []):
		return(syllables[0][-1].isdigit())

print(time()-start_time)


def articlechecker(word_bef,word,word_after):
	if(sounds_like_a_vowel(word_after) or starts_with_vowel_sound(word_after)):
		if(word_bef in punctuation_list):
			if(word == "an"):
				val1 = frequency_finder2("an",word_after)
				val2 = frequency_finder2("the",word_after)
				if(val1>1000):
					return word
				else:
					if(val1>=val2):
						return word
					else:
						return "the"
			else:
				val1 = frequency_finder2("an",word_after)
				val2 = frequency_finder2("the",word_after)
				if(val1>=val2):
					return "an"
				else:
					return "the"
		else:
			if(word == "an"):
				val1 = frequency_finder1(word_bef,"an",word_after)
				val2 = frequency_finder1(word_bef,"the",word_after)
				if(val1>1000):
					return word
				else:
					if(val1>=val2):
						return word
					else:
						return "the"
			else:
				val1 = frequency_finder1(word_bef,"an",word_after)
				val2 = frequency_finder1(word_bef,"the",word_after)
				if(val1>=val2):
					return "an"
				else:
					return "the"
						
	else:
		if(word_bef in punctuation_list):
			if(word == "an"):
				val1 = frequency_finder2("a",word_after)
				val2 = frequency_finder2("the",word_after)
				if(val1>1000):
					return word;
				else:
					if(val1>=val2):
						return word
					else:
						return "the"
			else:
				val1 = frequency_finder2("a",word_after)
				val2 = frequency_finder2("the",word_after)
				if(val1>=val2):
					return "a"
				else:
					return "the"
		else:
			if(word == "a"):
				val1 = frequency_finder1(word_bef,"a",word_after)
				val2 = frequency_finder1(word_bef,"the",word_after)
				if(val1>1000):
					return word
				else:
					if(val1>=val2):
						return word
					else:
						return "the"
			else:
				val1 = frequency_finder1(word_bef,"a",word_after)
				val2 = frequency_finder1(word_bef,"the",word_after)
				if(val1>=val2):
					return "a"
				else:
					return "the"
						

print(time()-start_time)


print(articlechecker("is","an","country"))