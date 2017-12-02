from django.contrib import admin
from .models import AnonymousTip, AnonymousUser

admin.site.register(AnonymousUser)
admin.site.register(AnonymousTip)
