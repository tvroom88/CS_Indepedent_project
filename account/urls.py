from django.urls import path
from account.views import (
	home_screen_view,
    registration_view,
    logout_view,
    login_view,
    account_view,
)


urlpatterns = [
    path('', home_screen_view, name="home"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('account/', account_view, name="account"),
]
