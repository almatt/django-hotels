from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('', HotelListApiView.as_view(), name="list"),
    path('<int:pk>/', HotelDetailApiView.as_view(), name="detail"),
    path('<int:pk>/update/', HotelUpdateApiView.as_view(), name="update"),
    path('<int:pk>/delete/', HotelDeleteApiView.as_view(), name="delete"),
    path('create/', HotelCreateApiView.as_view(), name="create")
]
