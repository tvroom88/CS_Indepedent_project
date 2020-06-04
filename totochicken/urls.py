from django.urls import path
from .views import (
    toto_restaurant_home_view,
    toto_menu_view,
    new_menu_view_board,



    toto_register_new_menu_view,

    # contactView,
    # successView,
    contact,
)

urlpatterns = [

    path('', toto_restaurant_home_view, name="toto_restaurant_home_view"),
    path('toto_menu/', toto_menu_view, name="toto_menu"),

    path('new_menu_board/', new_menu_view_board, name='toto_new_menu_board'),
    path('register_new_menu/', toto_register_new_menu_view, name='toto_register_new_menu'),

    path('contact/', contact, name='contact'),
    # path('success/', successView, name='success'),

]

