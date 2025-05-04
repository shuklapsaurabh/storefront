from django.urls import path
from . import views

# URL configuration for hello page
urlpatterns = [
    path('hello/', views.say_hello)
]