import sys
import re
import enchant

# US and UK dictionaries
# enchant dict objects
d_uk = enchant.Dict("en_UK")
d_us = enchant.Dict("en_US")
 
# reading input file 
file = sys.argv[1];
fo = open(file,"r")
fullfile = fo.read()
fullfile = fullfile.rsplit(".",1)[0]  # needs to be modified to handle ! and ? 
input_words= re.findall(r"[\w']+", fullfile)


def valid_word(word):
	return d_uk.check(word) or d_us.check(word)


for word in input_words :
	if(not valid_word(word)):
		print(word)

