from django.db import models
from django.forms import CharField,DateTimeField, DateField, NullBooleanField

# Create your models here.
class User(models.Model):
    user_key=models.CharField(max_length=50,blank=None, null=True)
    user_nickname=models.CharField(max_length=50,blank=None, null=True)
    user_name=models.CharField(max_length=50,blank=None, null=True)
    user_mbti=models.CharField(max_length=50)
    user_keyword1=models.CharField(max_length=50)
    user_keyword2=models.CharField(max_length=50)
    user_keyword3=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_status=models.IntegerField(default=0)
    register_dttm = models.DateTimeField(auto_now_add=True,verbose_name='가입시간')
    
    class Meta: #메타 클래스를 이용하여 테이블명 지정
        db_table = 'user'