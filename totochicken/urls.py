from django.urls import path
from totochicken.views import (
    toto_restaurant_home_view,
    toto_menu_view,
    # toto_contact_view,

    # contactView,
    # successView,
    contact,
)

urlpatterns = [

    path('', toto_restaurant_home_view, name="toto_restaurant_home_view"),
    path('toto_menu/', toto_menu_view, name="toto_menu"),
    # path('toto_contact/', toto_contact_view, name="toto_contact"),

    path('contact/', contact, name='contact'),
    # path('success/', successView, name='success'),

]
