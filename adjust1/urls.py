
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import  include

import AdjustApp

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('AdjustApp.urls'))
]
