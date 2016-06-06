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
        order_list = request.POST.get('order_list', '')

        try:
            models.Order.objects.create(name=name, street=street, house=house, corps=corps, building=building, number=number, phone=phone, email=email, company=company, order_list=order_list)

            return HttpResponse('OK')

        except:
            return HttpResponse('Error')

    else:
        all_products = models.Product.objects.all()
        fruits = []
        nuts = []

        for product in all_products:
            if product.the_type == "FRU":
                fruits.append(product)

            else:
                nuts.append(product)

        
        return render(request, template_name,
        {
            "page": { "title": title },
            'fruits': fruits,
            'nuts': nuts
        })
