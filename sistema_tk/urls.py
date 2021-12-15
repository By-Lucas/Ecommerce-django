
from django.contrib import admin
from django.urls import path, include
from usuarios.views import home, index_2
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')), #SERVE PARA TRANSFERIR AS URLS PARA URLS CRIADA NO APP USUARIOS
    path('inicio/', home),
    path('produtos/', include('produtos.urls')),
    path('login/', include('django.contrib.auth.urls'), name='login'),
] 


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)