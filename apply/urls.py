from django.urls import path
from .views import *

urlpatterns = [
    # 참여하기 버튼을 땅 눌렀을 때 발동
    path('', join_room, name='join_room'),
    
]