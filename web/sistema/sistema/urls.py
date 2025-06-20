from django.contrib import admin
from django.urls import path, include
from sistema.views import Login, Logout, LoginAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view(), name='login'),
    path('autenticacao-api/', LoginAPI.as_view()),
    path('logout/', Logout.as_view(), name='logout'),
    path('veiculo/', include('veiculo.urls'), name='veiculo'),
    path('anuncio/', include('anuncio.urls'), name='anuncio')
]
