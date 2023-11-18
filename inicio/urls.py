from django.urls import path
from inicio.views import inicio, usuario


urlpatterns = [
     path('', inicio, name="inicio"),
     path('usuario/', usuario, name="usuario"),
]