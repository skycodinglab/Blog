from django.urls import path
from  web_blog.views import Home

urlpatterns = [
    path('',Home, name='home'),
]