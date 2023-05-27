# Libraries and packages
from django.forms.widgets import DateInput
from website.choices import *
from website.models import *
from django import forms

# Calculator forms
class femaleCalculatorForm(forms.Form):
    petName = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre de tu mascota')
    age = forms.ChoiceField(choices = age, required = True, label = 'Edad')
    weight = forms.FloatField(min_value = 0.1, required = True, label = 'Peso')
    pregnant = forms.ChoiceField(choices = yes_no, required = True, label = '¿Tu perrita está embarazada?')
    brandName = forms.ChoiceField(choices = brands, required = True, label = 'Nombre del producto')

class maleCalculationForm(forms.Form):
    petName = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre de tu mascota')
    age = forms.ChoiceField(choices = age, required = True, label = 'Edad')
    weight = forms.FloatField(min_value = 0.1, required = True, label = 'Peso')
    brandName = forms.ChoiceField(choices = brands, required = True, label = 'Nombre del producto')

# Website forms
class contactForm(forms.Form):
    firstName = forms.CharField(min_length = 1, max_length = 50, required = True, label = 'Nombre(s)')
    lastName = forms.CharField(min_length = 1,  max_length = 50, label = 'Apellido(s)')
    email = forms.EmailField(required = True, label = 'Correo electrónico')
    message = forms.CharField(widget = forms.Textarea, min_length = 10, max_length = 2_000, required = True, label = 'Mensaje')

# Users and pets forms
class addUserForm(forms.Form):
    firstName = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre(s)')
    lastName = forms.CharField(min_length = 1, max_length = 30, label = 'Apellido(s)')
    email = forms.EmailField(required = True, label = 'Correo electrónico')

class editUserForm(forms.Form):
    firstName = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre(s)')
    lastName = forms.CharField(min_length = 1, max_length = 30, label = 'Apellido(s)')
    email = forms.EmailField(required = True, label = 'Correo electrónico')

class addPetForm(forms.Form):
    name = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre')
    birthday = forms.DateField(required = True, label = 'Fecha de nacimiento', widget = DateInput(attrs = {'type': 'date'}))
    breed = forms.ChoiceField(choices = breeds, required = True, label = 'Raza')
    sex = forms.ChoiceField(choices = sex, required = True, label = 'Sexo')

class editPetForm(forms.Form):
    name = forms.CharField(min_length = 1, max_length = 30, required = True, label = 'Nombre')
    birthday = forms.DateField(required = True, label = 'Fecha de nacimiento', widget = DateInput(attrs = {'type': 'date'}))
    breed = forms.ChoiceField(choices = breeds, required = True, label = 'Raza')
    sex = forms.ChoiceField(choices = sex, required = True, label = 'Sexo')