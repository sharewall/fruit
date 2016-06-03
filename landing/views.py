from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse

def index(request):
    template_name = 'landing/index.html'
    title = 'Фрукты'

    return render(request, template_name,
    {
        "page": { "title": title }
    })
    #return HttpResponse('It works!')
