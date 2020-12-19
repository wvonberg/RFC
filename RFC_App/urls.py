from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landingPage'),
    path('account/create/', views.signup, name='signup'),
    path('account/signin/', views.signin, name='signin'),
    path('account/signout/', views.signout, name='signout'),
    path('forum/', views.forum, name='forum'),
    path('add_post', views.add_post, name='add_post'),
    path('add_comment/<int:id>', views.add_comment),
    path('goto_post/<int:id>', views.single_post_page),
]
