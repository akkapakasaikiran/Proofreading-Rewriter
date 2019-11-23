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
from nltk import pos_tag
from nltk import word_tokenize
import verb
# import demo_pro
# import interro_pro
import article

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
pos_list = pos_tag(word_list)
print(pos_list)
#print(word_list)
correction = {}
article_list = {'a',"an"}

for i in range(len(word_list)-1):
	word = word_list[i].lower();
	word_bef = word_list[i-1]
	word_after = word_list[i+1]
	if(pos_list[i][1] == 'DT' and word in article_list):
		new_word = article.articlechecker(word_bef,word,word_after)
		if(word == new_word):
			continue
		else:
			correction[i] = new_word 
	elif(pos_list[i][1][:2] == 'VB'):
		#print("\n"+word)
		if(word_after in punctuation_list):
			new_word = verb.changetense2(word_before,word)
		else:
			new_word = verb.changetense3(word_bef,word,word_after)

		if(word == new_word):
			continue
		else:
			correction[i] = new_word
	# elif(pos_tag(word_tokenize(word))[0][1] == 'DT' and word not in article_list):
	# 	if(word_bef in punctuation_list):
	# 		new_word = demo_pro.change2(word,word_after)
	# 	else:
	# 		new_word = demo_pro.change3(word_bef,word,word_after)

	# 	if(word == new_word):
	# 		continue
	# 	else:
	# 		correction[i] = new_word
	# elif(pos_tag(word_tokenize(word))[0][1] == 'WP' or pos_tag(word_tokenize(word))[0][1] == 'NNP'):
	# 	if(word_before in punctuation_list):
	# 		new_word = interro_pro.change2(word,word_after)
	# 	else:
	# 		new_word = interro_pro.change3(word_bef,word,word_after)

		#if(word == new_word):
		#	continue
		#else:
		#	correction[i] = new_word
		
for k,v in correction.items():
	print("Correction in word no. {} is {}. ".format(k,v))