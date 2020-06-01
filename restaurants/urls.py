from django.urls import path
from restaurants.views import (
    register_new_menu_view,
    restaurant_view,
    register_restaurant_view,
    menu_board_view,
    menu_delete,
    menu_update,
)

urlpatterns = [




    path('', restaurant_view, name="restaurant_home_view"),
    path('register_new_restaurant/', register_restaurant_view, name="register_new_restaurant"),
    path('register_new_menu/', register_new_menu_view, name="register_new_menu"),
    path('menu_board/', menu_board_view, name="menu_board"),

    path('delete/', menu_delete, name="menu_delete"),
    # path('menu_update/', menu_update, name="menu_update"),
    path('menu_update/<int:pk>/', menu_update, name="menu_update"),
]

