from django.urls import path
from . import views
#register urls
urlpatterns = [
    path('insertuser/', views.insertuser, name='insertuser'),
    path('loginuser/', views.loginuser, name='loginuser'),
    ]