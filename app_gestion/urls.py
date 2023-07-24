from django.urls import path
from .views import indexGestionView, aboutView

urlpatterns = [
    path('',indexGestionView, name="index"),
    path('about',aboutView, name="about"),
]