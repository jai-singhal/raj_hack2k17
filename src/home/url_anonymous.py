from django.conf.urls import url, include

from .views import anonymous_tip, anonymous_user_login

urlpatterns = [

    url(r'^', anonymous_user_login, name='anonymous_user_login'),
    url(r'^tip', anonymous_tip, name='anonymous_tip'),

]
