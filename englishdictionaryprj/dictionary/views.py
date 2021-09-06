from django.shortcuts import render
from PyDictionary import PyDictionary

def home(request):
    return render(request, 'home.html')


def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    antonyms = dictionary.antonym(search)
    synonyms = dictionary.synonym(search)

    context = {
        'meaning': meaning['Noun'][0],
        'antonyms': antonyms,
        'synonyms': synonyms,
    }
    return render(request, 'word.html', context)
