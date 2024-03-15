from django.contrib import admin
from web_blog.models import Category,Tags,Post,CommentsPost,ReplyPost


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['id','name','banner_img','slug','created_date','update_date']

@admin.register(Tags)
class Tags(admin.ModelAdmin):
    list_display = ['id','name','created_date','update_date']

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['id','user','category','tag','post_title','slug','post_img','description',
                   'created_date','update_date']

@admin.register(CommentsPost)
class CommentsPost(admin.ModelAdmin):
    list_display = ['id','user','post','comment','created_date','update_date']

@admin.register(ReplyPost)
class ReplyPost(admin.ModelAdmin):
    list_display = ['id','user','comments','reply_comments','created_date','update_date']

