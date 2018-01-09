from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('', login_required(HotelList.as_view()), name='index'),
    path('<int:pk>/', login_required(HotelDetail.as_view()), name='details'),
    path('rate/', login_required(rate), name='rate'),
]
