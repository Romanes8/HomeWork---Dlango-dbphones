from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones_object = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phones_object = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones_object = Phone.objects.all().order_by('-price')
    else:
        phones_object = Phone.objects.all()
    template = 'catalog.html'
    context = {
        'phones': phones_object
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.filter(slug=slug)
    template = 'product.html'
    phone = {}
    for atr in phone_object:
        phone['name'] = atr.name
        phone['image'] = atr.image
        phone['price'] = atr.price
        phone['release_date'] = atr.release_date
        phone['lte_exists'] = atr.lte_exists
    context = {
        'phone': phone
    }
    return render(request, template, context)
