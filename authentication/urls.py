from django.urls import path
from .views import *

urlpatterns = [
    path('',user_login,name='login'),
    path('logout/',logout_user,name='logout'),
    path('Internlink/adduser', adduser,name='adduser'),
]
