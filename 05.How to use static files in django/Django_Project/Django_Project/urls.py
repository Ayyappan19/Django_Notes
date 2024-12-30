from django.contrib import admin
from django.urls import path

from My_Application import views
urlpatterns = [
    path('admin/', admin.site.urls),



      path('',views.home),

]
