

from frequency_finder import frequency_finder2
from frequency_finder import frequency_finder1

def change_after(w,d):
	cur_freq = frequency_finder2(w,d)
	print("cur freq ", cur_freq)
	if cur_freq > 10000 :
		return d
	else :
		alter = ['this','that','those','these']
		max_freq=0
		best = d
		for alt in alter:
			new_freq = frequency_finder2(w,alt)
			print(new_freq)
			if new_freq > max_freq :
				max_freq = new_freq
				best = alt
		return best

def change_before(d,w):
	cur_freq = frequency_finder2(d,w)
	print("cur freq ", cur_freq)
	if cur_freq > 10000 :
		return d
	else :
		alter = ['this','that','those','these']
		max_freq=0
		best = d
		for alt in alter:
			new_freq = frequency_finder2(alt,w)
			print(new_freq)
			if new_freq > max_freq :
				max_freq = new_freq
				best = alt
		return best
