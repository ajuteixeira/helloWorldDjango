from django.shortcuts import render

def hello(request):
    return render(request, 'meuapp/hello.html')
