
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from dashboard.models import Hotels
from .serializers import *

class HotelListApiView(ListAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelListSerializer

class HotelDetailApiView(RetrieveAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDetailSerializer

class HotelUpdateApiView(UpdateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelUpdateSerializer

class HotelDeleteApiView(DestroyAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDeleteSerializer

class HotelCreateApiView(CreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelDeleteSerializer


