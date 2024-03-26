from django.urls import path
from app.views import *

urlpatterns = [
    path('ping',ping),
    path('login/',login,name="login"),
    path('signup/',signup,name="signup"),
    path('logout/',logout,name="logout"),
    path('',dashboard,name="dashboard"),
]