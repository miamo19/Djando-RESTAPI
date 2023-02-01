#from django
from django.contrib import admin

#from project
from .models import Drink

@admin.register(Drink)
class AdminDrink(admin.ModelAdmin):
    pass
