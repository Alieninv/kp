
from django.contrib import admin
from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('person',Personview.as_view()),

    ]

