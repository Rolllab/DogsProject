from django.contrib import admin

from cats.models import Bread, Cat

@admin.register(Bread)
class BreadAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', )
    ordering = ('pk', )

@admin.register(Cat)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'bread',)
    list_filter = ('bread', )
    ordering = ('name', )