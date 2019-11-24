# What are you saying.
# Oh, I see!
# Why, that's a beautiful statement!
# Are you okay.
# Ahhh!
# 
# Well ... okay.
# I don't see any reason why.
# I see!
# is it okay. => Is it okay. and not Is it okay?

# if first word is wp or nnp then replace fullstop with question mark

import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
import enchant

def actual_punc(body):
	l = nltk.tokenize.sent_tokenize(body)
	print(l)
	sentence_list = []
	for sentence in l:
		pos_list = nltk.pos_tag(nltk.word_tokenize(sentence))
		pos_list = correct_punctuation(pos_list) # send a sentence to correct_punctuation
		only_words = [x for (x,y) in pos_list]
		sentence_list.append(TreebankWordDetokenizer().detokenize(only_words))
	return TreebankWordDetokenizer().detokenize(sentence_list)


d_uk = enchant.Dict("en_UK")
d_us = enchant.Dict("en_US")

def valid_word(word_inp):
	cap_word = word_inp.capitalize()
	return d_uk.check(word_inp) or d_us.check(word_inp) or d_us.check(cap_word) or d_uk.check(cap_word)  

def cap(unit):
	if unit[1]=="NNP" or unit[1]=="NNPS" or not valid_word(unit[0]):
		return (unit[0].capitalize(),unit[1])

def correct_punctuation(postags):
	if postags[0][1]=="NNP" or postags[0][1]=="WP" or postags[0][1]=="WRB" or postags[0][1]=="WDT":
		postags[len(postags)-1]=('?',".")
	if postags[0][1]=='UH' :
		postags[len(postags)-1]=('!','.')		
	for i in range(len(postags)):
		if cap(postags[i]) or postags[i][0]=='i' or i==0:
			postags[i] = (postags[i][0].capitalize(),postags[i][1]) 

	return postags

print(actual_punc("Did it really happen."))