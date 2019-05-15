from django.urls import path

from rest_framework import routers

from .views import Coins, CoinDetail, CoinSearch

urlpatterns = [
    path('api/coins/', Coins.as_view()),
    path('api/coin/<int:pk>', CoinDetail.as_view()),
    path('api/coin/<str:symbol>', CoinSearch.as_view())
]
