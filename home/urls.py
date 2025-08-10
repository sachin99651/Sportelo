from django.urls import path, include
from . import views
#home urls
urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_register, name='signup'), 
    path('user/',include('user.urls')),
    path('teamrankings/', views.teamrankings,name='teamrankings'), 
    path('menrankings/',views.menrankings,name='menrankings'),
    path('womenrankings/',views.womenrankings,name='womenrankings'),
]