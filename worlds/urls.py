
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
    path(
        'worlds/<int:world_id>/characters/create/',
        views.character_create,
        name='character_create'
    ),
    path(
        'worlds/<int:world_id>/characters/<int:character_id>/',
        views.character_detail,
        name='character_detail'
    ),
    path(
        'worlds/<int:world_id>/characters/<int:character_id>/edit/',
        views.character_update,
        name='character_update'
    ),
    path(
        'worlds/<int:world_id>/characters/<int:character_id>/delete/',
        views.character_delete,
        name='character_delete'
    ),
    path(
        'worlds/<int:world_id>/lore/create/',
        views.lore_entry_create,
        name='lore_entry_create'
    ),
    path(
        'worlds/<int:world_id>/lore/<int:lore_entry_id>/',
        views.lore_entry_detail,
        name='lore_entry_detail'
    ),
    path(
        'worlds/<int:world_id>/lore/<int:lore_entry_id>/edit/',
        views.lore_entry_update,
        name='lore_entry_update'
    ),
    path(
        'worlds/<int:world_id>/lore/<int:lore_entry_id>/delete/',
        views.lore_entry_delete,
        name='lore_entry_delete'
    ),
    path('worlds/public', views.public_world_list, name='public_world_list'),
]