from django.urls import path
from . import views


# Define URL patterns for the app
urlpatterns = [
    path('', views.index, name='index'),
]