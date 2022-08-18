from django.shortcuts import render
from PyDictionary import PyDictionary
from  .models import SearchedWords
def home(request):
    return render(request, 'home.html')


def word(request):
    search = request.GET.get('search')
    
    # Saving Searched Words To Database
    SearchedWords.objects.create(word=search)

    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    context = {
        'meaning': meaning['Noun'][0],
        'synonyms': synonyms,
        'antonyms': antonyms
    }
    return render(request, 'word.html', context)
