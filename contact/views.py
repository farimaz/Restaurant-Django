from django.shortcuts import render
from . import forms

# Create your views here.
def contact(request):
    contact_form = forms.ContactForm()
    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
        else:
            contact_form = forms.ContactForm()
    context={'form':contact_form}
    return render(request,'contact/contact.html',context)
    

