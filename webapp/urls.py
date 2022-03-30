import imp
from django.urls import path, include
from webapp import views
from webapp.views import Login, SignUp
urlpatterns = [
    path('', views.home, name='index.html'),
    path('home', views.home, name='home'),
    path('login', Login.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', SignUp.as_view(), name='signup'),
]
