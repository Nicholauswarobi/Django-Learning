from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success', views.contat_success_view, name='contat_success')
]