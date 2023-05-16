# Libraries and packages 
from django.shortcuts import render

# Website views
def home(request):
    return render(request, 'home.html')

def calculator(request):
    if request.method == 'POST':
        pass

    else:
        return render(request, 'calculator.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        pass

    else:
        return render(request, 'contact.html')

def search(request):
    pass

def signup(request):
    if request.method == 'POST':
        pass

    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        pass

    else:
        return render(request, 'login.html')

def logout(request):
    pass

# Users and pets views
def viewUserAccount(request):
    return render(request, 'userAccount.html')

def editUserAccount(request):
    pass

def delUserAccount(request):
    pass

def viewPets(request):
    return render(request, 'pets.html')

def addPet(request):
    pass

def editPet(request):
    pass

def delPet(request):
    pass