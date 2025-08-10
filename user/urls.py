from django.urls import path
from . import views
from home import views as vw
#home urls
urlpatterns = [
    path('profile', views.user_profile, name='profile'),
    path('matches/', views.user_matches, name='matches'),
    path('logout/', vw.index, name='logout'), 
    path('rankings/', views.rankings, name='rankings'),
    path('editprof/', views.user_editprof, name='editprof'),

    ]