from django.conf.urls import url
from django.conf.urls import include
from account.views import UserSignUP, LogInView




urlpatterns = [
    url(r'signup/',UserSignUP.as_view()),
    url(r'login/', LogInView.as_view()),
]
