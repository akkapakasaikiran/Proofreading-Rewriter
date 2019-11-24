import logging
import nltk
from django.shortcuts import render, get_object_or_404

from .models import Word
from .rewriter_program.spell_check import spell_suggestions

# Create your views here.


def index(request):
	if 'new_stop' not in request.POST:
		new_stop = 0
	else:
		new_stop = request.POST['new_stop']

	if 'inp' not in request.POST:
		sentence = ""
	else:
		sentence = request.POST['inp']
	
	prev_stop = request.session.get('prev_stop', '0')
	request.session['prev_stop'] = new_stop
	newint = int(new_stop)
	prevint = int(prev_stop)
	sub = sentence[prevint:newint-1]
	tokens = nltk.word_tokenize(sub)
	logging.debug(spell_suggestions(tokens))
	return render(request, 'rewrite_app/index.html', {'prev_stop': new_stop, 'sentence': sentence})


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
