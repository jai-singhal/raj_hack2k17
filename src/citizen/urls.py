from django.conf.urls import url, include
from django.views.generic import TemplateView
<<<<<<< HEAD
from .views import login_view, dashboard, register_view,create_case
=======
from .views import login_view, dashboard, register_view, citizen_logout
>>>>>>> 7d59336bce7c17d260927a30d6c9a915b4cd59f9

urlpatterns = [

    url(r'^$', login_view , name='login'),
    url(r'^logout$', citizen_logout , name='login'),
    url(r'^register$', register_view , name='login'),
<<<<<<< HEAD
    url(r'^dashboard/$', dashboard , name='dashboard'),
    url(r'^create_case/$', create_case , name='create_case'),
=======
    url(r'^dashboard/', dashboard , name='dashboard'),
>>>>>>> 7d59336bce7c17d260927a30d6c9a915b4cd59f9

]

