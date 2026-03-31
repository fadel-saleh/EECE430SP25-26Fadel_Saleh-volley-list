from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players/', views.player_list, name='player_list'),
    path('players/add/', views.add_player, name='add_player'),
    path('players/update/<int:pk>/', views.update_player, name='update_player'),
    path('players/delete/<int:pk>/', views.delete_player, name='delete_player'),
]