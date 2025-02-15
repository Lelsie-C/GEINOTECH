from django.contrib import admin
from .models import ProgrammingLanguage
from .models import Update 


# Register your models here.

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','link')  # Fields to display in the admin list view
    search_fields = ('name',)  # Adds a search bar for the 'name' field
    list_filter = ('name',)  # Adds a filter sidebar for the 'name' field

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'link')  # Fields to display in the admin list view
    search_fields = ('name',)  # Adds a search bar for the 'name' field
    list_filter = ('name',)  # Adds a filter sidebar for the 'name' field
