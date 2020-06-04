from django.contrib import admin
from .models import NewMenu


class MenuAdmin(admin.ModelAdmin):
	list_display = ('Menu', 'price', 'Info')
	search_fields = ('Menu', 'price')

admin.site.register(NewMenu, MenuAdmin)