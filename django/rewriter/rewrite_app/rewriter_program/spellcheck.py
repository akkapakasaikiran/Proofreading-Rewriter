import os
import sys
import re
import enchant
import math
from collections import Counter
from django.conf import settings

#global variable
word = ""

def words(text): return re.findall(r'\w+', text.lower())

big_txt_location = os.path.join(settings.BASE_DIR, 'rewrite_app/rewriter_program/big.txt')
WORDS = Counter(words(open(big_txt_location).read()))

# US and UK dictionaries as enchant dict objects
d_uk = enchant.Dict("en_UK")
d_us = enchant.Dict("en_US")

keyboard_cartesian = {'q': {'x':0, 'y':0}, 'w': {'x':1, 'y':0}, 'e': {'x':2, 'y':0}, 'r': {'x':3, 'y':0}, 't': {'x':4, 'y':0}, 'y': {'x':5, 'y':0}, 'u': {'x':6, 'y':0}, 'i': {'x':7, 'y':0}, 'o': {'x':8, 'y':0}, 'p': {'x':9, 'y':0}, 'a': {'x':0, 'y':1},'z': {'x':0, 'y':2},'s': {'x':1, 'y':1},'x': {'x':1, 'y':2},'d': {'x':2, 'y':1},'c': {'x':2, 'y':2}, 'f': {'x':3, 'y':1}, 'b': {'x':4, 'y':2}, 'm': {'x':6, 'y':2}, 'j': {'x':6, 'y':1}, 'g': {'x':4, 'y':1}, 'h': {'x':5, 'y':1}, 'j': {'x':6, 'y':1}, 'k': {'x':7, 'y':1}, 'l': {'x':8, 'y':1}, 'v': {'x':3, 'y':2}, 'n': {'x':5, 'y':2}, "'":{'x':1000, 'y':1000} }

subs_factor=0.5

# ignore stuff in body after last fullstop / question mark / exclamation mark
def only_sentences(body):
	lst1 = body.rsplit('.', 1);
	lst2 = body.rsplit('!', 1);
	lst3 = body.rsplit('?', 1);

	if (len(lst3[-1]) < len(lst1[-1]) and len(lst3[-1]) < len(lst2[-1])):
		body = lst3[0] + '?'
	elif ((len(lst1[-1]) < len(lst3[-1]) and len(lst1[-1]) < len(lst2[-1]))):
		body = lst1[0] + '.'
	else:
		body = lst2[0] + '!'
	return body

def valid_word(word_inp):
	cap_word = word_inp.capitalize()
	return d_uk.check(word_inp) or d_us.check(word_inp) or d_us.check(cap_word) or d_uk.check(cap_word)

def P(word,variate):
	#print("{}:{}".format(variate,WORDS[variate]/sum(WORDS.values())))
	if(WORDS[variate]==0):
		return 0.6*damerau_levenshtein_distance(word,variate)
	else:
		return 0.5*damerau_levenshtein_distance(word, variate) + 0.0001*sum(WORDS.values())/WORDS[variate] 

def correction(word_inp):
	"Most probable spelling corrections for word."
	possibilities=variations(word_inp)
	# possibilities2 = set()
	# global word 
	# real_word = word
	# for x in possibilities :
	# 	word = x
	# 	y = variations()
	# 	possibilities2 = set(list(possibilities2) + list(y)) 
	# possibilities = set(list(possibilities) + list(possibilities2))
	# word = real_word
	return list(filter(valid_word,sorted(possibilities, key=P)))

def euclidean_distance(a,b):
	X = (keyboard_cartesian[a]['x'] - keyboard_cartesian[b]['x'])**2
	Y = (keyboard_cartesian[a]['y'] - keyboard_cartesian[b]['y'])**2
	return math.sqrt(X+Y)

def variations(word):
	insert = []
	replace = []
	delete = []
	transpose = []
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	for i in range(len(word)):
		n = len(word);
		parts = [word[:i], word[i:]]
		for ch in alphabets:
			insert.append(parts[0] + ch + parts[1])
			replace.append(parts[0] + ch + parts[1][1:]) # parts[1][1:] == word[i + 1:]
		delete.append(parts[0] + parts[1][1:])
		if (i < n - 1): transpose.append(parts[0] + parts[1][1] + parts[1][0] + parts[1][2:])
	return set(delete + insert + replace + transpose);

def edit_distance(s1,s2):
	M = len(s1);
	N = len(s2);
	dp = {}
	for i in range(M + 1):
		for j in range(N + 1):
			if i == 0:
				dp[i, j] = j
			elif j == 0:
				dp[i, j] = i
			elif s1[i - 1] == s2[j - 1]:
				dp[i, j] = dp[i - 1, j - 1]
			else:
				dp[i, j] =  min(dp[i, j - 1]+1, dp[i - 1, j]+1, dp[i - 1, j - 1]+subs_factor*euclidean_distance(s1[i-1],s2[j-1]))
	return dp[M, N]

def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in  range(-1,lenstr2+1):
        d[(-1,j)] = j+1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = euclidean_distance(s1[i],s2[j])
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return d[lenstr1-1,lenstr2-1]


# reading input file
# fullfile = open(sys.argv[1], "r").read()
# fullfile = fullfile.lower()
# fullfile = re.sub(r'[0-9]', "", fullfile) # removing numbers
# input_words = re.findall(r"[\w']+", only_sentences(fullfile))
# input_words = [word.strip("'") for word in input_words] # "in 'my life'" -> in,my,life


#num_wrong_words=0
def spell_suggestions(word_inp):
#for word_inp in input_words:
	# print(word_inp)
	if valid_word(word_inp) : return []
	#num_wrong_words+=1
	return correction(word_inp)
	final_suggestions = correction() # works on global variable word
	print("Input word: {}".format(word_inp))
	print("Suggestions:{}".format(final_suggestions))
	print("")
	# for x in sorted(filter(valid_word,variations()),key=P):
	#  	print(x, edit_distance(word,x))
	# print("")
#if(num_wrong_words==0): print("Congrats on writing a completely error free peice of text!")

# word = "ddecidef"
# print("Input word: {}".format(word))
# print("Suggestions:{}".format(correction()))
# for x in sorted(filter(valid_word,variations()),key=P):
# 	print(x, edit_distance(word,x))