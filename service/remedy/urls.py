from django.urls import path
from .views import RemedyOrderListView


urlpatterns = [
    path('search-remedy/', RemedyOrderListView.as_view(), name='searc-remedy-list'),
] 
