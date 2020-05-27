from django.urls import path

from . import views

urlpatterns=[
    path('cotact', views.contact, name='contact')
]