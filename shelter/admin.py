from django.contrib import admin
from shelter.models import Animal
 # Register your models here.


@admin.register(Animal)
class AuthorAdmin(admin.ModelAdmin):
    pass