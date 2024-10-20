from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Подключаем URL-ы приложения blog
    path('games/', include('battleship.urls')),
]
