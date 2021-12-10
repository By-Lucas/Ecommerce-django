
from django.contrib import admin
from django.urls import path, include
from usuarios.views import home, index_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')), #SERVE PARA TRANSFERIR AS URLS PARA URLS CRIADA NO APP USUARIOS
    path('inicio/', home),
    path('login/', include('django.contrib.auth.urls'), name='login'),
]
