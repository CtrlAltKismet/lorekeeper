
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='worlds/login.html'),
        name='login'
    ),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('worlds/create/', views.world_create, name='world_create'),
    path('worlds/<int:world_id>/', views.world_detail, name='world_detail'),
    path('worlds/<int:world_id>/edit/', views.world_update, name='world_update'),
    path('worlds/<int:world_id>/delete/', views.world_delete, name='world_delete'),
]