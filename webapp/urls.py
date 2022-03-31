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
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('manage_members', views.manage_members, name='manage_members'),
    path('monthly_accounting', views.monthly_accounting, name='monthly_accounting'),
    path('bazar_details', views.bazar_details, name='bazar_details'),
    path('my_bazar_details', views.my_bazar_details, name='my_bazar_details'),
    path('my_meal_records', views.my_meal_records, name='my_meal_records'),
]
