from django.contrib import admin
from .models import Post
from .models import Comment



# Register your models here.

class CommentInline(admin.TabularInline):  # new
    model = Comment
   
class PostAdmin(admin.ModelAdmin):  # new
    inlines = [
    CommentInline,
]







admin.site.register(Post, PostAdmin)
admin.site.register(Comment)  


