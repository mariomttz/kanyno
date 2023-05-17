# Libraries and packages
from django import forms
from .models import *
from .choices import *

# Website forms
class calculatorForm(forms.Form):
    pass

class signupForm(forms.Form):
    name = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre')
    email = forms.EmailField(required = True, label = 'Correo electrónico')
    password1 = forms.CharField(min_length = 8, max_length = 16, required = True, label = 'Contraseña')
    password2 = forms.CharField(min_length = 8, max_length = 16, required = True, label = 'Repita su contraseña')

class loginForm(forms.Form):
    email = forms.EmailField(required = True, label = 'Correo electrónico')
    password = forms.CharField(min_length = 8, max_length = 16, required = True, label = 'Contraseña')

class contactForm(forms.Form):
    firstName = forms.CharField(min_length = 1, max_length = 50, required = True, label = 'Nombre(s)')
    lastName = forms.CharField(min_length = 1,  max_length = 50, label = 'Apellido(s)')
    email = forms.EmailField(required = True, label = 'Correo electrónico')
    message = forms.CharField(widget = forms.Textarea, min_length = 10, max_length = 2_000, required = True, label = 'Mensaje')

# Users and pets forms
class editUserForm(forms.Form):
    pass

class addPetForm(forms.Form):
    name = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre')
    birthday = forms.DateField(required = True, label = 'Fecha de nacimiento')
    breed = forms.ChoiceField(choices = breeds, required = True, label = 'Raza')
    sex = forms.ChoiceField(choices = sex, required = True, label = 'Sexo')

class editPetForm(forms.Form):
    pass