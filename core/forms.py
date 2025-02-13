from django import forms 
from django.shortcuts import render 

from .forms import ContactForm 

from .models import Contact 

from .models import CV 

 

class ContactForm(forms.ModelForm): 

    class Meta: 

        model = Contact 

        fields = ['name', 'email', 'message'] 

def contact_view(request): 

    if request.method == "POST": 

        form = ContactForm(request.POST) 

        if form.is_valid(): 

            name = form.cleaned_data['name'] 

            email = form.cleaned_data['email'] 

            message = form.cleaned_data['message'] 

            # You can process the form data (e.g., save to DB, send an email) 

            return render(request, 'success.html', {'name': name}) 

    else: 

        form = ContactForm() 

 

    return render(request, 'contact.html', {'form': form}) 

class CVForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False)  

    class Meta:
        model = CV
        fields = ['name', 'email', 'profile_picture']