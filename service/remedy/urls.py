from django.urls import path
from .views import RemedyOrderCreateListView


urlpatterns = [
    path('remedys/', RemedyOrderCreateListView.as_view(), name='remedys-create-list'),
] 
