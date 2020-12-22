from django.contrib import admin
from .models import Post, Support, Profile, Comment, Request, Profile

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Support)
admin.site.register(Request)
admin.site.register(Profile)
