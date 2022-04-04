from django.urls import path, include
from .views import *

urlpatterns = [
    path("packages/", GetPackage.as_view()),
]