from django.shortcuts import render

# Create your views here.
import json, re

from django.views   import View
from django.http    import JsonResponse, HttpResponse
from .models        import User
from allauth.socialaccount.models import SocialAccount

def login(request):
    return render(request,'index.html')

def detailsignin(request):
    if request.method=='POST':
        #body =  json.loads(request.body.decode('utf-8'))
        #social_login_id=SocialAccount.objects.filter(user=request.user)[0].extra_data['id']
        #gg_id = SocialAccount.objects.filter(user=request.user, provider='google').uid
        new_User=User.objects.create(
            user_key=   request.user.id,
            user_nickname       =  request.POST.get("USER_NICKNAME"),
            user_name       =  request.POST.get("USER_NAME"),
            user_mbti       =  request.POST.get("USER_MBTI"),
            user_keyword1       =  request.POST.get("USER_KEYWORD1"),
            user_keyword2       =  request.POST.get("USER_KEYWORD2"),
            user_keyword3       =  request.POST.get("USER_KEYWORD3"),
            user_email       =  request.POST.get("USER_EMAIL")
        )
        
        return render(request,'success.html')
    else:
        return render(request,'SigninSheet.html')

