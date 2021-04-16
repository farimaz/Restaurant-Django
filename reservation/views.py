from django.shortcuts import render
from . import forms

# Create your views here.
def reservation(request):
    reserve_form=forms.ResevationForm()
    if request.method == "POST":
        reserve_form = forms.ResevationForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
        else:
            reserve_form = forms.ResevationForm()
    context={'form':reserve_form}
    return render(request,'reservation/reservation.html',context)