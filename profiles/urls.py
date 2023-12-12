from django.urls import path
from .views import Register, user_login, user_logout, profile, pass_change, set_pass

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/password_change', pass_change, name='pass_change'),
    path('profile/set_password', set_pass, name='set_pass'),
]
