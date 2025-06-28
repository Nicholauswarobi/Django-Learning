from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

def home_view(request):
    return render(request, 'forms_app/home.html')

# Define the contact_view function to handle the contact form
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contat_success')
        
    else:
        form = ContactForm()

    context = {'form':form}

    return render(request, 'forms_app/contact.html', context)


# Define contact_success_view function to handle the success page
def contat_success_view(request):
    return render(request, 'forms_app/contact_success.html')