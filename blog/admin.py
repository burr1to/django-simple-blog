from django.contrib import admin
from . import models

# Register your models here.

class adminAuth(admin.ModelAdmin):
    list_display = ('blog_title','blog_date','blog_author')
    
admin.site.register(models.Post,adminAuth)
