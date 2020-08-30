from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def password(request):
    import random
    passw =""
    char = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))

    if request.GET.get('upper'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        char.extend(list('!@#$%^&*()'))
    
    if request.GET.get('number'):
        char.extend(list('0123456789'))

    for i in range(length+1):
        passw+=random.choice(char)
    
    return render(request,'password.html',{'password':passw})
