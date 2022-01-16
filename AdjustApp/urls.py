from django.urls import re_path
from AdjustApp import views

urlpatterns = [
    re_path(r'^adjustapi/$', views.root_),
    
]