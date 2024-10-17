# battleship/urls.py
from django.urls import path
from .views import index, game_view  # Обновляем 'game' на 'game_view'

urlpatterns = [
    path('', index, name='battleship_index'),  # Главная страница игры
    path('game/<int:game_id>/', game_view, name='game'),  # Страница самой игры
]
