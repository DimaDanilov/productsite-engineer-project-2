from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import Products, Salerman
from .serializers import ProductsSerializer
from .forms import ProductForm, PriceFilterForm
from rest_framework.response import Response
from rest_framework.views import APIView


class ProductsView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response({"products": serializer.data})

    def post(self, request):
        products = request.data.get('product')
        serializer = ProductsSerializer(data=products)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.title)})


def index(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error="Форма не валидна"

    products = Products.objects.all()
    workers = Salerman.objects.all()
    formsort = PriceFilterForm(request.GET)

    if formsort.is_valid():
        if formsort.cleaned_data['price_min']:
            products = products.filter(price__gte=formsort.cleaned_data['price_min'])

        if formsort.cleaned_data['price_max']:
            products = products.filter(price__lte=formsort.cleaned_data['price_max'])

    form = ProductForm()
    context = {
        'products': products,
        'formsort': formsort,
        'form': form,
        'error': error,
        'workers': workers
    }
    return render(request, 'main/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form' : form}
    return render(request, 'registration/register.html', context)