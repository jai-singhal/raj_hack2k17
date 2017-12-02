
from django.conf.urls import url
from django.contrib import admin
from comment.views import CreateComment
from comment.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'comment/ajax/create', CreateComment, name = "create_comment"),
    url(r'^$', HomePage, name = "home")
]
