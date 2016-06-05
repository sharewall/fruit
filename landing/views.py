from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from . import models

def index(request):
    template_name = 'landing/index.html'
    title = 'Фрукты'

    if request.method == 'POST':
        name = request.POST.get('name', '')
        street = request.POST.get('street', '')
        house = request.POST.get('house', '')
        corps = request.POST.get('corps', '')
        building = request.POST.get('building', '')
        number = request.POST.get('number', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        company = request.POST.get('company', '')

        try:
            models.Order.objects.create(name=name, street=street, house=house, corps=corps, building=building, number=number, phone=phone, email=email, company=company)

            return HttpResponse('OK')

        except:
            return HttpResponse('Error')

    else:
        return render(request, template_name,
        {
            "page": { "title": title }
        })
