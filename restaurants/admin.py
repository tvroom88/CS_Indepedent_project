from django.contrib import admin
from restaurants.models import Menu, Restaurant


class MenuAdmin(admin.ModelAdmin):
	list_display = ('restaurant', 'Menu', 'price', 'Info')
	search_fields = ('restaurant', 'Menu', 'price',)

admin.site.register(Menu, MenuAdmin)

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('owner', 'restaurant_name', 'phone')
	search_fields = ('owner', 'restaurant_name','phone')
admin.site.register(Restaurant, RestaurantAdmin)
#
#
	# filter_horizontal = ()
	# list_filter = ()
	# fieldsets = ()
#
