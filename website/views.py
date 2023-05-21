# Libraries and packages 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from website.auxiliaryFunctions import *
from website.models import *
from website.forms import *

# Website views
def home(request):
    return render(request, 'home.html')

def calculator(request):
    if request.method == 'POST':
        pass

    else:
        form = calculatorForm()

        return render(request, 'calculator.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        pass

    else:
        try:
            username = request.user
            userInfo = usuarios.objects.get(user = username)
            firstName = userInfo.nombre
            lastName = userInfo.apellido
            email = userInfo.correo
            form = contactForm(initial = {'firstName': firstName, 'lastName': lastName, 'email': email})

            return render(request, 'contact.html', {'form': form})

        except:
            form = contactForm()

            return render(request, 'contact.html', {'form': form})

def search(request):
    if request.method == 'POST':
        pass

def signup(request):
    if request.method == 'POST':
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            username = request.POST['username']

            try:
                user = User.objects.create_user(username = username, password = pass1)
                user.save()
                login(request, user)

                return redirect('add-account')

            except:
                form = UserCreationForm()
                error = 'El nombre de usuario no está disponible.'

                return render(request, 'signup.html', {'form': form, 'error': error})
        else:
            form = UserCreationForm()
            error = 'Las contraseñas no coinciden, inténtalo de nuevo.'

            return render(request, 'signup.html', {'form': form, 'error': error})
    else:
        form = UserCreationForm()

        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)

            return redirect('home')

        else:
            form = AuthenticationForm()
            error = 'El nombre de usuario o la contraseña son incorrectos. Intenta de nuevo.'

            return render(request, 'signin.html', {'form': form, 'error': error})
    else:
        form = AuthenticationForm()

        return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)

    return redirect('home')

# Users and pets views
def viewUserAccount(request):
    username = request.user
    userInfo = usuarios.objects.get(user = username)

    return render(request, 'userAccount.html', {'userInfo': userInfo})

def addUserAccount(request):
    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        username = request.user

        user = usuarios.objects.create(nombre = firstName, apellido = lastName, correo = email, user = username)
        user.save()

        return redirect('home')

    else:
        form = addUserForm()

        return render(request, 'addUserAccount.html', {'form': form})

def editUserAccount(request, username = None):
    if request.method == 'POST':
        userId = request.POST['userId']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']

        user = usuarios.objects.get(user = userId)
        user.nombre = firstName
        user.apellido = lastName
        user.correo = email
        user.save()

        return redirect('account')

    else:
        user = usuarios.objects.get(user = username)
        firstName = user.nombre
        lastName = user.apellido
        email = user.correo
        form = editUserForm(initial = {'firstName': firstName, 'lastName': lastName, 'email': email})

        return render(request, 'editUser.html', {'user': user, 'form': form})

def changePassword(request):
    if request.method == 'POST':
        pass

    else:
        user = request.user
        form = PasswordChangeForm(user)
        
        return render(request, 'changePassword.html', {'form': form})

def delUserAccount(request, username):
    user = User.objects.get(username = username)
    user.delete()

    return redirect('home')

def viewPets(request):
    if request.method == 'GET':
        try:
            username = request.user
            user = usuarios.objects.get(user = username)
            Pets = perros.objects.filter(clave_de_cuenta = user)
            formAdd = addPetForm()
            formEdit = editPetForm()

            return render(request, 'pets.html', {'Pets': Pets, 'formAdd': formAdd, 'formEdit': formEdit})

        except:
            formAdd = addPetForm()
            formEdit = editPetForm()

            return render(request, 'pets.html', {'formAdd': formAdd, 'formEdit': formEdit})

def addPet(request):
    if request.method == 'POST':
        name = request.POST['name']
        birthday = request.POST['birthday']
        breed = request.POST['breed']
        sex = request.POST['sex']

        username = request.user
        user = usuarios.objects.get(user = username)
        userId = usuarios.objects.get(user = username).clave_de_cuenta
        petId = dogKey(name, userId)

        pet = perros.objects.create(
            clave_de_mascota = petId, 
            nombre = name,
            fecha_de_nacimiento = birthday, 
            raza = breed,
            sexo = sex,
            clave_de_cuenta = user
            )
        pet.save()

        return redirect('pets')

def editPet(request, petId = None):
    if request.method == 'POST':
        petId = request.POST['petId']
        name = request.POST['name']
        birthday = request.POST['birthday']
        breed = request.POST['breed']
        sex = request.POST['sex']

        pet = perros.objects.get(clave_de_mascota = petId)
        pet.nombre = name
        pet.fecha_de_nacimiento = birthday
        pet.raza = breed
        pet.sexo = sex
        pet.save()

        return redirect('pets')

    else:
        pet = perros.objects.get(clave_de_mascota = petId)
        name = pet.nombre
        birthday = pet.fecha_de_nacimiento
        breed = pet.raza
        sex = pet.sexo

        form = editPetForm(initial = {'name': name, 'birthday': birthday, 'breed': breed, 'sex': sex})

        return render(request, 'editPet.html', {'pet': pet, 'form': form})

def delPet(request, petId):
    pet = perros.objects.get(clave_de_mascota = petId)
    pet.delete()

    return redirect('pets')