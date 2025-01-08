from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, LoginForm, CarForm, OrderForm
from .models import Car, Order
from django.utils import timezone

def index(request):
    context = {
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, 'index.html', context)

def data_base(request):
    car_form = CarForm()
    service_record_form = OrderForm()

    if request.method == 'POST':
        if 'car_form' in request.POST:
            car_form = CarForm(request.POST)
            if car_form.is_valid():
                car_form.save()
                return redirect('data_base')
        elif 'service_record_form' in request.POST:
            service_record_form = OrderForm(request.POST)
            if service_record_form.is_valid():
                service_record_form.save()
                return redirect('data_base')

    context = {
        'car_form': car_form,
        'service_record_form': service_record_form,
    }
    return render(request, 'data_base.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def data_table(request):
    cars = Car.objects.all()
    service_records = Order.objects.all()
    context = {
        'cars': cars,
        'service_records': service_records,
    }
    return render(request, 'data_table.html', context)

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('data_table')
    return render(request, 'delete_confirm.html', {'object': car})

def delete_service_record(request, record_id):
    record = get_object_or_404(Order, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('data_table')
    return render(request, 'delete_confirm.html', {'object': record})

def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('data_table')
    else:
        form = CarForm(instance=car)
    return render(request, 'edit_form.html', {'form': form})

def edit_service_record(request, record_id):
    record = get_object_or_404(Order, id=record_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('data_table')
    else:
        form = OrderForm(instance=record)
    return render(request, 'edit_form.html', {'form': form})