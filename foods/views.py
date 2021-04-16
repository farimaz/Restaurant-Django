from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
    food_list = models.Foods.objects.order_by('pub_date')
    context = {'food_list': food_list}
    return render(request,'foods/index.html',context)

def detail(request,id):
    food = get_object_or_404(models.Foods,id=id)
    context = {'food_detail':food}
    return render(request,'foods/detail.html',context)