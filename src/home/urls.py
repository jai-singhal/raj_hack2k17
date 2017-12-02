from django.conf.urls import url, include

urlpatterns = [

    url(r'^anonymous$', anonymous_tip , name='anonymous_tip'),
]
