import requests
import urllib
import json
import string
import sys
import re
import nltk
#from time import time
#start_time = time()
from frequency_finder import frequency_finder2
from frequency_finder import frequency_finder1
#print(time()-start_time)
import verb
#print(time()-start_time)
# import demo_pro
import interro
#print(time()-start_time)
import article
#print(time()-start_time)
import demopro
#print(time()-start_time)


result = string.punctuation

result = result.replace(' ', '')
punctuation_list = []
for i in range(len(result)):
    punctuation_list.append(result[i])
vowels = ['a','e','i','o','u'];


#input_file = sys.argv[1];
#f = open(input_file);


#word_string = f.read()

def grammar_checker(word_list)
#word_list = nltk.word_tokenize(word_string);
	pos_list = nltk.pos_tag(word_list)
	correction = {}
	article_list = ['a',"an"]
	demo_list = ['this','that','those','these']

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
			print("verb ", word)
			if(word_after in punctuation_list):
				new_word = verb.changetense2(word_before,word)
			else:
				new_word = verb.changetense3(word_bef,word,word_after)
			if(word == new_word):
				continue
			else:
				correction[i] = new_word
		elif(i==0 or pos_list[i-1][1] == 'WP' and word_bef in punctuation_list):
			new_word = interro.change_new1(word,word_after)
			if(word == new_word):
				continue
			else:
				correction[i] = new_word
		elif(i==0 or pos_list[i-1][1] == 'WP$' and word_bef in punctuation_list ):
			new_word = interro.change_new2(word,word_after)
			if(word == new_word):
				continue
			else:
				correction[i] = new_word
		elif(i==0 or pos_list[i-1][1] == 'WRB' and word_bef in punctuation_list):
			new_word = interro.change_new3(word,word_after)
			if(word == new_word):
				continue
			else:
				correction[i] = new_word
		elif(pos_list[i][1]=='DT' and word in demo_list):
			if(i==0 or word_bef in punctuation_list):
				new_word = demopro.change_before(word,word_after)
			elif(word_after in punctuation_list):
				new_word = demopro.change_after(word_bef,word)

			if(word == new_word):
				continue
			else:
				correction[i] = new_word


	return correction		
#for k,v in correction.items():
#	print("Correction in word no. {} is {}. ".format(k,v))
