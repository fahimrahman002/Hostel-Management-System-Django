import imp
from django.urls import path, include
from webapp import views
from webapp.views import Login, SignUp,Dashboard
urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard', Dashboard.as_view(), name='dashboard'),
    path('login', Login.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', SignUp.as_view(), name='signup'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('manage_members', views.manage_members, name='manage_members'),
    path('monthly_accounting', views.monthly_accounting, name='monthly_accounting'),
    path('all_bazar_details', views.all_bazar_details, name='all_bazar_details'),
    path('all_investments', views.all_investments, name='all_investments'),
    path('my_investments', views.my_investments, name='my_investments'),
    path('my_bazar_details', views.my_bazar_details, name='my_bazar_details'),
    path('my_meal_records', views.my_meal_records, name='my_meal_records'),
]
