# Libraries and packages
from django.urls import path
from .views import *

urlpatterns = [
    # Website URLs
    path('',            home,       name = 'home'),
    path('calculator/', calculator, name = 'calculator'),
    path('about/',      about,      name = 'about'),
    path('contact/',    contact,    name = 'contact'),
    path('search/',     search,     name = 'search'),
    path('signup/',     signup,     name = 'signup'),
    path('login/',      login,      name = 'login'),
    path('logout/',     logout,     name = 'logout'),

    # Users and pets URLs
    path('account/',        viewUserAccount, name = 'account'),
    path('account/edit/',   editUserAccount, name = 'edit-account'),
    path('account/delete/', delUserAccount,  name = 'del-account'),
    path('pets/',           viewPets,        name = 'pets'),
    path('pets/add/',       addPet,          name = 'add-pet'),
    path('pets/edit/',      editPet,         name = 'edit-pet'),
    path('pets/delete/',    delPet,          name = 'del-pet'),
]