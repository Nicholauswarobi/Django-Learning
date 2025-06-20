from django.shortcuts import render
from .models import Tour


# Create your views here.
def home(request):
    tours_variable = Tour.objects.all()
    context = {'tours': tours_variable}
    return render(request, 'tours/home.html', context)
