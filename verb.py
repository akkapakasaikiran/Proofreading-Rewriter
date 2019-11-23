from pattern.en import conjugate, lemma, lexeme,PRESENT,SG
from frequency_finder import frequency_finder1
from frequency_finder import frequency_finder2

def changetense3(l,c,r):
	print("\nyo")
	# print()
	# print("imput verb is '"+c+"'")
	cur_freq = frequency_finder1(l,c,r)
	if cur_freq > 1500 :
		return c
	else :
		verbs = lexeme(c)
		max_freq=0
		for v in verbs:
			new_freq = frequency_finder1(l,v,r)
			print(v,new_freq)
			if new_freq > max_freq :
				max_freq = new_freq
				best_verb = v
		return best_verb

def changetense2(l,c):
	print("\nyo2")
	# print("imput verb is "+c)
	cur_freq = frequency_finder2(l,c)
	if cur_freq > 1500 :
		return c
	else :
		verbs = lexeme(c)
		max_freq=0
		for v in verbs:
			new_freq = frequency_finder2(l,v)
			print(v,new_freq)
			if new_freq > max_freq :
				max_freq = new_freq
				best_verb = v
		return best_verb
# print(lexeme("try"))
# print(changetense3("I", "play", "football"))
# print(changetense3("I", "playing", "football"))
# print(changetense3("He", "am", "good"))
# print(changetense3("He", "plays", "football"))
# print(changetense2("He", "play"))

# print(changetense3("He", "is", "nice"))
# sprint(changetense3("I", "is", "nice"))
# print(changetense3("He", "am", "nice"))

# print([changetense(x) for x in inp])

