from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.

def home(request):
    return render(request, 'base.html')

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products':products})

@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        catagory = request.POST.get('catagory')
        stock = request.POST.get('stock')

        if name and price :
            Product.objects.create(
                name=name,
                price=price,
                catagory=catagory,
                stock=stock,
            )
            return redirect('index')
    return render(request, 'add.html')

@login_required
def edit(request, product_id):
    x = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        catagory = request.POST.get('catagory')
        stock = request.POST.get('stock')

        if name and price :
            x.name = name
            x.price = price
            x.catagory = catagory
            x.stock = stock
            x.save()
            return redirect('index')
    return render(request, 'edit.html',{'product':x})

@login_required
def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('index')

# Authentication
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def admin_page(request):
    if request.user.is_superuser:
        return HttpResponse("Welcome Admin")
    else:
        return HttpResponse("Only Admin Allowed")



   #=====================   REST API    ========================= 


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

# Post
@api_view(['POST'])
def product_create(request):
    serializer = ProductSerializer(data=request.data) #get data from client
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)