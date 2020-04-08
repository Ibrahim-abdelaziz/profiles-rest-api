from django.conf.urls import url
from django.conf.urls import include
from account.views import UserSignUP, LogInView




urlpatterns = [
    url('signup/',UserSignUP.as_view()),
    url('login/', LogInView.as_view()),
]
