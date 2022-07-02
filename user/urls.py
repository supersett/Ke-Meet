from django.urls import path, include
from .views import *
from user.views import login,detailsignin

app_name='user'

urlpatterns = [
    path('login/',login,name='login'),
    path('detailsignin/',detailsignin,name='detailsignin'),
]

