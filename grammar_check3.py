import requests
import urllib
import json
import string
import sys
import re
import nltk
from time import time
start_time = time()

#import csv

print(time()-start_time)


from frequency_finder import frequency_finder2
from frequency_finder import frequency_finder1

print(time()-start_time)

#from nltk import pos_tag
#from nltk import word_tokenize
import verb
# import demo_pro
# import interro_pro
import article


print(time()-start_time)
result = string.punctuation

result = result.replace(' ', '')
punctuation_list = []
for i in range(len(result)):
    punctuation_list.append(result[i])
vowels = ['a','e','i','o','u'];

print(time()-start_time)

input_file = sys.argv[1];
f = open(input_file);

print(time()-start_time)

word_string = f.read()

print(time()-start_time)

word_list = nltk.word_tokenize(word_string);
pos_list = nltk.pos_tag(word_list)
print(pos_list)

print(time()-start_time)


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

return correction		
# for k,v in correction.items():
# 	print("Correction in word no. {} is {}. ".format(k,v))