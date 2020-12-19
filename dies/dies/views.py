from django.shortcuts import render
import os

def homepage(request):
    
    return render(request, 'dies/homepage.html')


def shutdown(request):
    os.system('sudo shutdown -h now')
    return render(request, 'dies/base.html')