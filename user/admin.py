from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display=('user_key','user_nickname','user_name','user_mbti','user_keyword1','user_keyword2','user_keyword3','user_email','user_status','register_dttm')

admin.site.register(User,UserAdmin)