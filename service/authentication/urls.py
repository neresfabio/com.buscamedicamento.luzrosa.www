from django.urls import path
from .views import CustomUserCreateListView


urlpatterns = [
    path('users/', CustomUserCreateListView.as_view(), name='users-create-list'),
] 
