from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Foods)
class FoodsAdmin(admin.ModelAdmin):
    list_display=('name','price','time')
