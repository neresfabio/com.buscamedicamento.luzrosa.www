from rest_framework import generics
from .models import RemedyOrder
from .serializers import RemedyOrderSerializer


class RemedyOrderCreateListView(generics.ListCreateAPIView):
    queryset = RemedyOrder.objects.all()
    serializer_class = RemedyOrderSerializer