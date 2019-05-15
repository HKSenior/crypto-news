from rest_framework import permissions, generics
from rest_framework.response import Response

from .serializers import CoinSerializer
from .models import Coin


class Coins(generics.ListCreateAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class CoinDetail(generics.RetrieveAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer


class CoinSearch(generics.ListAPIView):
    serializer_class = CoinSerializer

    def list(request, *args, **kwargs):
        sym = kwargs.get('symbol')

        if sym:
            queryset = Coin.objects.filter(
                symbol__contains=sym.upper()
            ).filter(symbol__startswith=sym.upper())
            serializer = CoinSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
