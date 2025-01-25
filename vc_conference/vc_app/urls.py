from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.myregister),
    path('login',views.mylogin,name='mylogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('meeting',views.runvc,name='meeting'),
    path('logout',views.mylogout,name='logout'),
    path('joinroom',views.joinroom,name='joinroom'),


]
