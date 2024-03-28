from django.contrib import admin
from .models import Video, Comment, Avatar, Embed


admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Embed)
admin.site.register(Avatar)

