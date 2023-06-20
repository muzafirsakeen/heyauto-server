from . import views
from django.urls import path

urlpatterns = [

    path('',views.admin,name='home'),
    path('home',views.login_admin,name="home"),
    path('drivers',views.driverspage,name="drivers"),
    path('dashboard',views.dashboard,name="dashboard"),
    
    path('requests',views.requests,name="requests"),
    path('notification',views.notification,name="notification"),

]
