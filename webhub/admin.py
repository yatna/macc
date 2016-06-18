from django.contrib import admin
from malaria.models import Post, RevPost
from webhub.models import *

admin.site.register(Post)
admin.site.register(RevPost)

