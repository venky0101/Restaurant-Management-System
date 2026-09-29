from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FoodForm

from .models import FoodItem


def home(request):
    foods = FoodItem.objects.all()

    return render(
        request,
        'menu/home.html',
        {'foods': foods}
    )


def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        user.save()

        messages.success(request, 'Registration successful')
        return redirect('login')

    return render(request, 'menu/register.html')
def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'menu/login.html')
def user_logout(request):

    logout(request)

    return redirect('login')

def add_food(request):

    if request.method == 'POST':

        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = FoodForm()

    return render(request, 'menu/add_food.html', {'form': form})

def edit_food(request, id):

    food = FoodItem.objects.get(id=id)

    if request.method == 'POST':

        form = FoodForm(
            request.POST,
            request.FILES,
            instance=food
        )

        if form.is_valid():
            form.save()
            return redirect('home')

    else:

        form = FoodForm(instance=food)

    return render(
        request,
        'menu/edit_food.html',
        {'form': form}
    )
def delete_food(request, id):

    food = FoodItem.objects.get(id=id)

    food.delete()

    return redirect('home')