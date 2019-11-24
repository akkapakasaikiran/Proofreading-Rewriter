# A big bad wolf vs a bad big wolf
#  a beautiful big white bulldog vs white beautiful big 
# an amazing new movie vs a new amazing movie 
# IMP : do article check AFTER adj order check

import itertools
from frequency_finder import frequency_finder1
from frequency_finder import frequency_finder4

def order3(a1,a2,n):
	if frequency_finder1(a2,a1,n) > frequency_finder1(a1,a2,n):
		return (a2,a1,n)
	else :
		return (a1,a2,n)

def order4(a1,a2,a3,n):
	perms=itertools.permutations([a1,a2,a3])
	max_freq=0
	best_order=[]
	for perm in perms:
		cur_freq = frequency_finder4(perm[0],perm[1],perm[2],n)
		if cur_freq > max_freq:
			max_freq = cur_freq
			best_order=perm
	return (best_order[0],best_order[1],best_order[2]) 



