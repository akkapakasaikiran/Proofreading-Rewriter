from pattern.en import lexeme
from frequency_finder import frequency_finder1
from frequency_finder import frequency_finder2
is_verb_full = lexeme("is")
is_verb_full.remove('be')
is_verb_full.remove('being')
is_verb_full.remove('been')
is_verb_pos = is_verb_full[:5]
is_verb_neg = is_verb_full[5:]

def changetense3(l,c,r):
	cur_freq = frequency_finder1(l,c,r)
	if cur_freq > 1500 :
		return c
	else :
		if(c not in is_verb_full):
			verbs = lexeme(c)
			max_freq=0
			best_verb = c
			for v in verbs:
				new_freq = frequency_finder1(l,v,r)
				if new_freq > max_freq :
					max_freq = new_freq
					best_verb = v
			return best_verb
		else:
			if(c in is_verb_pos):
				verbs = is_verb_pos
				max_freq=0
				best_verb = c
				for v in verbs:
					new_freq = frequency_finder1(l,v,r)
					if new_freq > max_freq :
						max_freq = new_freq
						best_verb = v
				return best_verb
			else:                   ##must be in is_verb_neg
				verbs = is_verb_neg
				max_freq=0
				best_verb = c
				for v in verbs:
					new_freq = frequency_finder1(l,v,r)
					if new_freq > max_freq :
						max_freq = new_freq
						best_verb = v
				return best_verb

def changetense2(l,c):
	cur_freq = frequency_finder2(l,c)
	if cur_freq > 100000:
		return c
	else :
		if(c not in is_verb_full):
			verbs = lexeme(c)
			max_freq=0
			best_verb = c
			for v in verbs:
				new_freq = frequency_finder2(l,v)
				if new_freq > max_freq :
					max_freq = new_freq
					best_verb = v
			return best_verb
		else:
			if(c in is_verb_pos):
				verbs = is_verb_pos
				max_freq=0
				best_verb = c
				for v in verbs:
					new_freq = frequency_finder2(l,v)
					if new_freq > max_freq :
						max_freq = new_freq
						best_verb = v
				return best_verb
			else:                   ##must be in is_verb_neg
				verbs = is_verb_neg
				max_freq=0
				best_verb = c
				for v in verbs:
					new_freq = frequency_finder2(l,v)
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

