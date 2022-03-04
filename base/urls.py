from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('info/', views.info, name='info'),

    path('', views.home, name='home'),
    path('post/<str:pk>/', views.post, name='post'),

    path('school-board/', views.schoolDashBoard, name='school-board'),

    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),
    path('delete-post/<str:pk>/', views.deletePost, name='delete-post'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
]