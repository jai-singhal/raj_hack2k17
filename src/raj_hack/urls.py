
from django.conf.urls import url, include
from django.contrib import admin
from comment.views import CreateComment
from comment.views import HomePage, CommentPage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^police/', include('police.urls')),
    url(r'^anonymous/', include('home.url_anonymous')),
    url(r'^citizen/', include('citizen.urls')),
    url(r'comment/ajax/create', CreateComment, name = "create_comment"),
    url(r'comment/', CommentPage, name = "comment"),
    url(r'^$', HomePage, name = "HomePage")

]
