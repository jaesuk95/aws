from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    user_type = models.IntegerField() 
    
    
    
    # 0 은 사용자를 뜻한다, 1: 사장님, 2:배달기사
    # 사용자를 추가하기 위해서는 INSOMNIA 에 들어가서 URL 를 입렵한다 http://127.0.0.0:8000/user/user/
    # 이후, POST 를 입력해 "name":"사용자", "user_type": "0"


