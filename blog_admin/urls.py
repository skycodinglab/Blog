from django.urls import path
from blog_admin.views import index

app_name = 'blog_admin'

urlpatterns=[
        path('deshboard/admin', index.as_view(), name = 'index'),
 ]