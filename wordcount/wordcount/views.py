from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    num = len(fulltext.split())
    wordDictionary = {}
    for word in fulltext.split():
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1

    sortedList = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
    count_dict = {'fulltext':fulltext, 'num':num, 'wordDictionary': sortedList}
    return render(request, 'count.html', context=count_dict)

def about(request):
    return render(request, 'about.html')