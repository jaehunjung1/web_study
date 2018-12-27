from django.shortcuts import render

# Create your views here.
def index(request):
    insertdict = {'insert_me':'Hello Django!'}
    return render(request, 'first_app/index.html', context=insertdict)