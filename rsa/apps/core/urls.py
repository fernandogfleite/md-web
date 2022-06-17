from django.urls import path
from rsa.apps.core import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('chave/', views.generate_public_key_view, name='chave'),
    path('encriptar/', views.encrypt_view, name='encriptar'),
    path('desencriptar/', views.decrypt_view, name='desencriptar'),
]