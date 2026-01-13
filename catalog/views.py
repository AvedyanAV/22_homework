from django.shortcuts import render
from django.http import HttpResponse
from  .models import Product


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        return HttpResponse(f'Спасибо {name} сообщение получено')
    return render(request, 'catalog/contacts.html')


def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'catalog/product.html', context)