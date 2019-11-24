from frequency_finder import frequency_finder2

def change_new1(p,w):
	cur_freq = frequency_finder2(p,w)
	print("cur freq ", cur_freq)
	if cur_freq > 10000 :
		return p
	else :
		alter = ['what','who','whom']
		max_freq=0
		for alt in alter:
			new_freq = frequency_finder2(alt,w)
			print(new_freq)
			if new_freq > max_freq :
				max_freq = new_freq
				best = alt
		return best

def change_new2(p,w):
	cur_freq = frequency_finder2(p,w)
	if cur_freq > 10000 :
		return p
	else :
		alter = ['whose','which']
		max_freq=0
		for alt in alter:
			new_freq = frequency_finder2(alt,w)
			if new_freq > max_freq :
				max_freq = new_freq
				best = alt
		return best

def change_new3(p,w):
	cur_freq = frequency_finder2(p,w)
	if cur_freq > 10000 :
		return p
	else :
		alter = ['when','where','how','why']
		max_freq=0
		for alt in alter:
			new_freq = frequency_finder2(alt,w)
			if new_freq > max_freq :
				max_freq = new_freq
				best = alt
		return best