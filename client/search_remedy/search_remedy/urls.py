from django.urls import path
from app_search_remedy import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    path('',views.home,name='home'),
]
