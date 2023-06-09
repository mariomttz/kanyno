# Libraries and packages
from django.urls import path
from website.views import *

urlpatterns = [
    # Website URLs
    path('',                   home,       name = 'home'),
    path('calculator/',        calculator, name = 'calculator-post'),
    path('calculator/<petId>', calculator, name = 'calculator-get'),
    path('about/',             about,      name = 'about'),
    path('contact/',           contact,    name = 'contact'),
    path('search/',            search,     name = 'search'),
    path('signup/',            signup,     name = 'signup'),
    path('signin/',            signin,     name = 'signin'),
    path('signout/',           signout,    name = 'signout'),

    # Users and pets URLs
    path('account/',                  viewUserAccount,  name = 'account'),
    path('account/add/',              addUserAccount,   name = 'add-account'),
    path('account/edit/',             editUserAccount,  name = 'edit-account-post'),
    path('account/edit/<userId>',     editUserAccount,  name = 'edit-account-get'),
    path('account/edit/password/',    changePassword,   name = 'change-password'),
    path('account/delete/<username>', delUserAccount,   name = 'del-account'),
    path('pets/',                     viewPets,         name = 'pets'),
    path('pets/add/',                 addPet,           name = 'add-pet'),
    path('pets/edit/',                editPet,          name = 'edit-pet-post'),
    path('pets/edit/<petId>',         editPet,          name = 'edit-pet-get'),
    path('pets/delete/<petId>',       delPet,           name = 'del-pet'),
]

# URLs for errors
handler404 = 'website.views.error404'
handler500 = 'website.views.error500'