from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Comments)
class CommentsAdmin(admin.ModelAdmin):
    pass