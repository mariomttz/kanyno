# Libraries and packages 
from django.shortcuts import render
from .forms import *

# Website views
def home(request):
    return render(request, 'home.html')

def calculator(request):
    if request.method == 'POST':
        pass

    else:
        form = calculatorForm()
        return render(request, 'calculator.html', {
            'form': form
            })

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        pass

    else:
        form = contactForm()
        return render(request, 'contact.html', {
            'form': form
            })

def search(request):
    if request.method == 'POST':
        pass

def signup(request):
    if request.method == 'POST':
        pass

    else:
        form = signupForm()
        return render(request, 'signup.html', {
            'form': form
            })

def login(request):
    if request.method == 'POST':
        pass

    else:
        form = loginForm()
        return render(request, 'login.html',{
            'form': form
            })

def logout(request):
    pass

# Users and pets views
def viewUserAccount(request):
    if request.method == 'GET':
        form = editUserForm()
        return render(request, 'userAccount.html', {
            'form': form
            })

def editUserAccount(request):
    pass

def delUserAccount(request):
    pass

def viewPets(request):
    if request.method == 'GET':
        formAdd = addPetForm()
        formEdit = editPetForm()
        return render(request, 'pets.html', {
            'formAdd': formAdd,
            'formEdit': formEdit
            })

def addPet(request):
    pass

def editPet(request):
    pass

def delPet(request):
    pass