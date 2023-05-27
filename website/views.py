# Libraries and packages 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.core.validators import validate_email, ValidationError
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from website.auxiliaryFunctions import *
from datetime import datetime
from website.models import *
from website.forms import *

# Website views
def home(request):
    return render(request, 'home.html')

def calculator(request, petId = None):
    if request.method == 'POST':
        sex = request.POST['sex']

        if sex == 'Hembra':
            form = femaleCalculatorForm(request.POST)

            if form.is_valid():
                pregnant = form.cleaned_data['pregnant']
                age = form.cleaned_data['age']

                if pregnant == 'Si':
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = pregnant_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

                elif age == 'Cachorro':
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = little_puppy_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

                elif age == 'Adulto':
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = adult_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

                else:
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = old_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

            else:
                pet = perros.objects.get(clave_de_mascota = petId)
                sex = pet.sexo
                petId = pet.clave_de_mascota
                name = pet.nombre
                timeNow = datetime.now()
                birthday = pet.fecha_de_nacimiento
                birthdayYear = int(birthday.strftime('%Y'))
                currentYear = int(timeNow.strftime('%Y'))
                age = dogAge(currentYear, birthdayYear)
                form = maleCalculationForm(initial = {'petName': name, 'age': age, 'brandName': 'Otro'})
                error = 'Los datos ingresados no son válidos, por favor, inténtalo de nuevo.'

                return render(request, 'calculator.html', {'error': error, 'petId': petId, 'sex': sex, 'form': form})

        else:
            form = maleCalculationForm(request.POST)

            if form.is_valid():
                age = form.cleaned_data['age']

                if age == 'Cachorro':
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = little_puppy_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

                elif age == 'Adulto':
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = adult_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

                else:
                    brandName = form.cleaned_data['brandName']
                    weight = form.cleaned_data['weight']
                    grammage = old_kcal(weight)
                    timeNow = datetime.now()
                    calculationDate = timeNow.strftime('%Y-%m-%d')
                    petId = request.POST['petId']
                    pet = perros.objects.get(clave_de_mascota = petId)

                    petCalculation = gramajes.objects.create(
                        nombre_producto = brandName,
                        gramaje = grammage,
                        fecha_de_calculo = calculationDate,
                        clave_de_mascota = pet
                    )

                    petCalculation.save()

                    return redirect('pets')

            else:
                pet = perros.objects.get(clave_de_mascota = petId)
                sex = pet.sexo
                petId = pet.clave_de_mascota
                name = pet.nombre
                timeNow = datetime.now()
                birthday = pet.fecha_de_nacimiento
                birthdayYear = int(birthday.strftime('%Y'))
                currentYear = int(timeNow.strftime('%Y'))
                age = dogAge(currentYear, birthdayYear)
                form = maleCalculationForm(initial = {'petName': name, 'age': age, 'brandName': 'Otro'})
                error = 'Los datos ingresados no son válidos, por favor, inténtalo de nuevo.'

                return render(request, 'calculator.html', {'error': error, 'petId': petId, 'sex': sex, 'form': form})

    else:
        pet = perros.objects.get(clave_de_mascota = petId)
        sex = pet.sexo

        if sex == 'Hembra':
            petId = pet.clave_de_mascota
            name = pet.nombre
            timeNow = datetime.now()
            birthday = pet.fecha_de_nacimiento
            birthdayYear = int(birthday.strftime('%Y'))
            currentYear = int(timeNow.strftime('%Y'))
            age = dogAge(currentYear, birthdayYear)
            form = femaleCalculatorForm(initial = {'petName': name, 'age': age, 'pregnant': 'No', 'brandName': 'Otro'})

            return render(request, 'calculator.html', {'petId': petId, 'sex': sex, 'form': form})

        else:
            petId = pet.clave_de_mascota
            name = pet.nombre
            timeNow = datetime.now()
            birthday = pet.fecha_de_nacimiento
            birthdayYear = int(birthday.strftime('%Y'))
            currentYear = int(timeNow.strftime('%Y'))
            age = dogAge(currentYear, birthdayYear)
            form = maleCalculationForm(initial = {'petName': name, 'age': age, 'brandName': 'Otro'})

            return render(request, 'calculator.html', {'petId': petId, 'sex': sex, 'form': form})

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            validate_email(email)
            form = contactForm(request.POST)

            if form.is_valid():
                subject = 'Dudas Kanyno'
                body = {
                    'firstName': form.cleaned_data['firstName'],
                    'lastName': form.cleaned_data['lastName'],
                    'email': form.cleaned_data['email'],
                    'message': form.cleaned_data['message'],
                }
                message = '\n'.join(body.values())

                try:
                    send_mail(subject, message, 'mariomttz@comunidad.unam.mx', ['mariomttz@comunidad.unam.mx'])
                    alert = 'El correo ha sido enviado exitosamente.'

                    return render(request, 'contact.html', {'form': form, 'alert': alert})

                except BadHeaderError as e:
                    form = contactForm()
                    error = 'Ha ocurrido un error al enviar el correo, por favor, inténtalo de nuevo.'
                        
                    return render(request, 'contact.html', {'form': form, 'error': error})

            else:
                form = contactForm()
                error = 'Los datos ingresados no son válidos, por favor, inténtalo de nuevo.'

                return render(request, 'contact.html', {'form': form, 'error': error})

        except ValidationError as e:
            form = contactForm()
            error = f'El correo electrónico {email} no es válido, por favor, ingrésalo de nuevo.'

            return render(request, 'contact.html', {'form': form, 'error': error})

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
        search_field = request.POST['search-field'].lower()

        urlViews = {
            'inicio': 'home',
            'acerca': 'about',
            'contacto': 'contact',
            'cuenta': 'account',
            'mascotas': 'pets'
        }
        
        try:
            view = urlViews[search_field]

            return redirect(view)

        except:
            return render(request, 'searchError.html', {'search_field': search_field})

def signup(request):
    if request.method == 'POST':
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        pass1_lenght = len(pass1)
        pass2_lenght = len(pass2)

        if pass1_lenght >= 8 and pass2_lenght >= 8:
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
            error = 'Tu contraseña debe ser de al menos 8 caracteres, por favor, inténtalo de nuevo.'

            return render(request, 'signup.html', {'form': form, 'error': error})

    else:
        form = UserCreationForm()

        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_lenght = len(password)

        if password_lenght >= 8:
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
            error = 'Tu contraseña debe ser de al menos 8 caracteres, por favor, inténtalo de nuevo.'

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
        email = request.POST['email']
        
        try:
            validate_email(email)
            form = addUserForm(request.POST)

            if form.is_valid():
                firstName = form.cleaned_data['firstName']
                lastName = form.cleaned_data['lastName']
                email = form.cleaned_data['email']
                username = request.user

                user = usuarios.objects.create(nombre = firstName, apellido = lastName, correo = email, user = username)
                user.save()

                return redirect('home')

            else:
                form = addUserForm()
                error = 'Los datos ingresados no son válidos, por favor, inténtalo de nuevo.'

                return render(request, 'addUserAccount.html', {'form': form, 'error': error})

        except ValidationError as e:
            form = addUserForm()
            error = f'El correo electrónico {email} no es válido, por favor, ingrésalo de nuevo.'

            return render(request, 'addUserAccount.html', {'form': form, 'error': error})

    else:
        form = addUserForm()

        return render(request, 'addUserAccount.html', {'form': form})

def editUserAccount(request, userId = None):
    if request.method == 'POST':
        email = request.POST['email']

        try:
            validate_email(email)
            form = editUserForm(request.POST)

            if form.is_valid():
                userId = request.POST['userId']
                firstName = form.cleaned_data['firstName']
                lastName = form.cleaned_data['lastName']
                email = form.cleaned_data['email']

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
                error = 'Los datos ingresados no son válidos, por favor, inténtalo de nuevo.'

                return render(request, 'editUser.html', {'user': user, 'form': form, 'error': error})

        except ValidationError as e:
            user = usuarios.objects.get(user = username)
            firstName = user.nombre
            lastName = user.apellido
            email = user.correo
            form = editUserForm(initial = {'firstName': firstName, 'lastName': lastName, 'email': email})
            error = f'El correo electrónico {email} no es válido, por favor, ingrésalo de nuevo.'

            return render(request, 'editUser.html', {'user': user, 'form': form, 'error': error})

    else:
        user = usuarios.objects.get(user = userId)
        firstName = user.nombre
        lastName = user.apellido
        email = user.correo
        form = editUserForm(initial = {'firstName': firstName, 'lastName': lastName, 'email': email})

        return render(request, 'editUser.html', {'user': user, 'form': form})

def changePassword(request):
    if request.method == 'POST':
        old_pass = request.POST['old_password']
        new_pass1 = request.POST['new_password1']
        new_pass2 = request.POST['new_password2']
        new_pass1_lenght = len(new_pass1)
        new_pass2_lenght = len(new_pass2)

        if new_pass1_lenght >= 8 and new_pass2_lenght >= 8:
            if new_pass1 == new_pass2:
                user = request.user
                form = PasswordChangeForm(user, request.POST)

                if form.is_valid():
                    userUpdate = form.save()
                    update_session_auth_hash(request, userUpdate)

                    return redirect('home')

                else:
                    user = request.user
                    form = PasswordChangeForm(user)
                    error = 'Tu contraseña antigua no coincide con la registrada en Kanyno, por favor, inténtalo de nuevo.'

                    return render(request, 'changePassword.html', {'form': form, 'error': error})

            else:
                user = request.user
                form = PasswordChangeForm(user)
                error = 'Tus nuevas contraseñas no coinciden, por favor, inténtalo de nuevo.'

                return render(request, 'changePassword.html', {'form': form, 'error': error})

        else:
            user = request.user
            form = PasswordChangeForm(user)
            error = 'Tu nueva contraseña debe ser de al menos 8 caracteres, por favor, inténtalo de nuevo.'

            return render(request, 'changePassword.html', {'form': form, 'error': error})

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
        username = request.user
        user = usuarios.objects.get(user = username)
        pets = perros.objects.filter(clave_de_cuenta = user)

        petsCalculations = []

        for pet in pets:
            petId = pet.clave_de_mascota

            try:
                petsCalculations.append(gramajes.objects.get(clave_de_mascota = petId))

            except:
                continue

        formAdd = addPetForm()
        formEdit = editPetForm()

        return render(request, 'pets.html', {'pets': pets, 'formAdd': formAdd, 'petsCalculations': petsCalculations, 'formEdit': formEdit})

def addPet(request):
    if request.method == 'POST':
        form = addPetForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            breed = form.cleaned_data['breed']
            sex = form.cleaned_data['sex']

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

        else:
            return redirect('pets')


def editPet(request, petId = None):
    if request.method == 'POST':
        form = editPetForm(request.POST)

        if form.is_valid():
            petId = request.POST['petId']
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            breed = form.cleaned_data['breed']
            sex = form.cleaned_data['sex']

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
            error = 'Los datos ingresados no son válidos, por favor, inténtalo de nuevo.'

            return render(request, 'editPet.html', {'pet': pet, 'form': form, 'error': error})

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

# Errors website views

def error404(request, exception):
    return render(request, '404.html')

def error500(request):
    return render(request, '500.html')