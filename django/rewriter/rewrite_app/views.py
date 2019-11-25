import logging
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
from django.shortcuts import render, get_object_or_404

from .models import Word
from .rewriter_program.spell_check import spell_suggestions

# Create your views here.


def index(request):

	if 'inp' not in request.POST:
		sentence = ""
	else:
		sentence = request.POST['inp']

	if 'spells' not in request.POST:
		spellid = '-1'
	else:
		spellid = request.POST['spells']

	ignore = request.session.get('ignore', [])

	if 'ignoreid' in request.POST:
		ignore.append(request.POST['ignoreid'])
		spellid = request.POST['ignoreid']
		request.session['ignore'] = ignore

	tokens = nltk.word_tokenize(sentence)

	if 'change' in request.POST:
		logging.debug(request.POST['change'])
		spellid = request.POST['changeid']
		tokens[int(spellid)]=request.POST['change']
		sentence = TreebankWordDetokenizer().detokenize(tokens)

	spells = spell_suggestions(tokens)

	for i in ignore:
		spells[int(i)] = []

	if int(spellid) not in spells:
		spells = []
	else:
		spells = spells[int(spellid)]

	return render(request, 'rewrite_app/index.html', {'sentence': sentence, 'spells': spells, 'tokens': tokens, 'spellid': spellid})


def spell(request, word_id):
    word_list = Word.objects.order_by('word_pos')
    word = get_object_or_404(Word, pk=word_id)
    spell_list = spell_suggestions(word.word_text)
    next_id = min(len(word_list), word_id + 1)
    prev_id = max(1, word_id - 1)
    context = {'word_list': word_list, 'spell_list': spell_list, 'next_id': next_id, 'prev_id': prev_id}
    return render(request, 'rewrite_app/spell.html', context)


def input(request):
    return render(request, 'rewrite_app/input.html')
