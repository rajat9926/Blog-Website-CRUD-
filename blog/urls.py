from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deletepost/<int:postid>/', views.delete_post, name='deletepost'),
    path('editpost/<int:postid>/', views.edit_post, name='editpost'),
]