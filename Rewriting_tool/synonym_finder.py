import requests
import urllib
import json
import string
import sys
import re
import nltk
import csv
from nltk.tokenize import word_tokenize

lingo = {"arbit": ["arbitrary",],
        "bandi": ["girl",],
        "chamka": ["understood", "understand",],
        "DAC": ["Disciplinary Action Committee",],
        "dadda": ["Dual Degree student",],
        "DoSA": ["Dean of Student Affairs",],
        "enthu": ["enthusiasm", "enthusiastic"],
        "farra": ["FR",],
        "freshie": ["first year student",],
        "fundae": ["tips", "tricks", "teeps and treekz",],
        "infi": ["infinite", "infinitely",],
        "insti": ["institute",],
        "junta": ["people",],
        "polt": ["politics",],
        "bc": ["branch change",]}

result = string.punctuation

result = result.replace(' ', '')
#print(result);
punctuation_list = []
for i in range(len(result)):
    punctuation_list.append(result[i])
#print(punctuation_list)

def jprint(obj,orig_word):
    # create a formatted string of the Python JSON object
    l = []
    for distro in obj:
        #if(nltk.pos_tag(list(orig_word))[0][1]==nltk.pos_tag(list(distro['word']))[0][1]):
        l.append(distro['word']);
       # print(l)
    return l
def P(variate):
    return variate[1]

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


output_words2 = []

tag_list = ['DT','PRP','VBD','IN','CC','VBZ','VBP']

def synonym_finder(word_list):
    correction = {}

    for i in range(len(word_list)):
        if word_list[i] in lingo:
            correction[i] = lingo[word_list[i]]
        elif(nltk.pos_tag(word_tokenize(word_list[i]))[0][1] in tag_list):
            continue
        elif(word_list[i] not in punctuation_list):

            a = "https://api.datamuse.com/words?rel_syn=" + word_list[i]
            word1 = ""
            word2 = ""
            word3 = ""
            if(i==0):
                a = a + "&rc=" + word_list[i+1]
                word3 = word_list[i+1]
            else:
                if(word_list[i-1] not in punctuation_list and word_list[i-1] not in lingo.keys()):
                    a = a + "&lc=" + word_list[i-1]
                    word1 = word_list[i-1]

                if(word_list[i+1] not in punctuation_list and word_list[i+1] not in lingo.keys()):
                    a = a + "&rc=" + word_list[i+1]
                    word3 = word_list[i+1]
            a = a + "&max=4"
           # print(a)
         #   print("out of loop")
            response = requests.get(a)
          #  print("completed parsing")
            dict_final = response.json()
            x = jprint(dict_final,word_list[i])
         #   print("x computed")
          #  print(x)
            #if(len(x)==0):
             #   x.append(word_list[i])
           # print(x)
            y = []
        #    print(x)
            for syn in x:
            #	print("search started")
            	b = "https://api.phrasefinder.io/search?corpus=eng-us&query=" + urllib.parse.quote(word1 + " " + syn + " " + word3) + "&format=tsv"
            #	print("Search ended")
            	phrasefinder = requests.get(b)
            	ans = phrasefinder.text
            	val = 0
            	if len(ans)>0:
            		for row in ans.split('\n'):
            			if len(row) > 0:
            				spl = row.split()
            				val += int(spl[len(spl)-6])
            	if val>3000:
            		y.append([syn,val])

            
            y = sorted(y,key=P,reverse=True)
            if(not(len(y)==0)):
                lst = [x[0] for x in y]
                correction[i] = lst

    return correction

def synonym_finder2(word_list,i):
    correction = {}
    
    if word_list[i] in lingo:
        correction[i] = lingo[word_list[i]]
    elif(nltk.pos_tag(word_tokenize(word_list[i]))[0][1] in tag_list):
        pass
    elif(word_list[i] not in punctuation_list):
       # print("coming")
        a = "https://api.datamuse.com/words?rel_syn=" + word_list[i]
        word1 = ""
        word2 = ""
        word3 = ""
       # print("In loop 2")
        if(i==0):
          #  print("in loop 3")
            a = a + "&rc=" + word_list[i+1]
            word3 = word_list[i+1]
        else:
            if(word_list[i-1] not in punctuation_list and word_list[i-1] not in lingo.keys()):
                a = a + "&lc=" + word_list[i-1]
                word1 = word_list[i-1]


            if(word_list[i+1] not in punctuation_list and word_list[i+1] not in lingo.keys()):
                a = a + "&rc=" + word_list[i+1]
                word3 = word_list[i+1]
        a = a + "&max=4"
       # print(a)
     #   print("out of loop")
        response = requests.get(a)
      #  print("completed parsing")
        dict_final = response.json()
        x = jprint(dict_final,word_list[i])
     #   print("x computed")
      #  print(x)
        #if(len(x)==0):
         #   x.append(word_list[i])
       # print(x)
        y = []
    #    print(x)
        for syn in x:
        #	print("search started")
        	b = "https://api.phrasefinder.io/search?corpus=eng-us&query=" + urllib.parse.quote(word1 + " " + syn + " " + word3) + "&format=tsv"
        #	print("Search ended")
        	phrasefinder = requests.get(b)
        	ans = phrasefinder.text
        	val = 0
        	if len(ans)>0:
        		for row in ans.split('\n'):
        			if len(row) > 0:
        				spl = row.split()
        				val += int(spl[len(spl)-6])
        	if val>3000:
        		y.append([syn,val])

        
        y = sorted(y,key=P,reverse=True)
        if(not(len(y)==0)):
            lst = [x[0] for x in y]
            correction[i] = lst

    return correction


#print(synonym_finder(nltk.word_tokenize("This is an implicit way and not the preferred one.")))
