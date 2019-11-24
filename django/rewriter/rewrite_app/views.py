import logging
from django.shortcuts import render, get_object_or_404

from .models import Word
from .rewriter_program.spellcheck import spell_suggestions

# Create your views here.


def index(request):
    inp = request.POST['inp']
    logging.debug(inp)
    word_list = Word.objects.order_by('word_pos')
#    spell_list = ['ABC']
#    spell_list = spell_suggestions(Word.objects.get(pk=1).word_text)
    context = {'word_list': word_list}
    return render(request, 'rewrite_app/index.html', context)


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
