from django.contrib import admin

from dogs.models import Bread, Dog

@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    ordering = ('pk', )

@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'bread',)
    list_filter = ('bread', )
    ordering = ('name', )