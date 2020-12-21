from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='landingPage'),
    path('account/create/', views.signup, name='signup'),
    path('account/signin/', views.signin, name='signin'),
    path('account/signout/', views.signout, name='signout'),
    path('forum/', views.forum, name='forum'),
    path('add_post', views.add_post, name='add_post'),
    path('add_comment', views.add_comment),
    path('add_comment_forum', views.add_comment_forum),
    path('goto_post/<int:id>', views.single_post_page),
    path('rules', views.rules, name='rules'),
    path('speakeasy', views.speakeasy, name='speakeasy'),
    path('techsupport',views.techsupport, name='techsupport'),
    path('arena', views.arena, name='arena')
]
