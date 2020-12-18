from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landingPage'),
    path('account/create/', views.signup, name='signup'),
    path('account/signin/', views.signin, name='signin'),
    path('account/signout/', views.signout, name='signout')
]
