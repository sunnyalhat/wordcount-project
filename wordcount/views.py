from django.http import HttpResponse
from django.shortcuts import render
import operator


def index(request):
    return render(request, 'index.html', {'id': '117'})


def wordcount(request):
    return render(request, 'wordcount.html')


def count(request):
    content = request.GET['txtContent']
    wordlist = content.split()

    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'content': content, 'wordcount': len(wordlist), 'sorted_words': sorted_words})

def about(request):
    return render(request, 'about.html')