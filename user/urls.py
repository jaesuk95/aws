from django.urls import path
from user import views

urlpatterns = [
    path('user/', views.user, name="user"),    # name 을 지은 이유는 url 에 이름을 다는것이다 
    path('login/', views.login, name="login")


]