from django.shortcuts import render
from .models import User

# Create your views here.
def home(request):
    return render(request, 'loginapp/home.html')

def verify(request):
    get_id = request.GET['loginid']
    get_password = request.GET['password']

    for user in User.objects.all():
        if (user.loginid == get_id):
            if (user.password == get_password):
                return render(request, 'loginapp/success.html', {'user':user})
    
    return render(request, 'loginapp/home.html')