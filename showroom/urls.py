from django.urls import path
from . import views

app_name = 'showroom'

urlpatterns = [
    path('', views.showroomhome, name='showroom'),
    path('pg/', views.pghome, name='pg'),
    path('pg/generatedpw/', views.password, name='generatedpw'),
    path('authsystem/', views.authhome, name='authhome'),
    path('authsystem/signupuser/', views.signupuser, name='signupuser'),
    path('authsystem/loginuser/', views.loginuser, name='loginuser'),
    path('authsystem/loggedinuser/', views.loggedinuser, name='loggedinuser'),
    path('authsystem/logout/', views.logoutuser, name='logoutuser'),
]