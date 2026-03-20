from django.contrib import admin

# Register your models here.
from .models import User, Cycle, Topic, Post, Article, Comment, Poll

admin.site.register(User, admin.ModelAdmin)
admin.site.register(Cycle, admin.ModelAdmin)
admin.site.register(Topic, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(Article, admin.ModelAdmin)
admin.site.register(Comment, admin.ModelAdmin)
admin.site.register(Poll, admin.ModelAdmin)