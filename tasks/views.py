from django.shortcuts import render
from django.http import HttpResponse

def helloWorld(request):

    return HttpResponse("Hello World!")


def taskList(request):

    return render(request, 'tasks/list.html')


def userName(request, name):

    return render(request, 'tasks/username.html', {'name': name})
