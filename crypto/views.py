import requests
import json

from django.shortcuts import render

from news.models import News


def index(request):
    # Price Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,EOS,LTC,XRP,NEO,QTUM,ZEC,BCH,DASH&tsyms=USD"
    )

    # Get articles from db
    records = News.objects.all()[:25]

    context = {        
        'price': json.loads(price_request.content),
        'news': list(records)
    }
    return render(request, 'pages/index.html', context)


def prices(request):
    if request.method == 'POST':
        # Get form data
        quote = request.POST['quote'].upper()        

        # Get currency data
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD"
        )

        context = {
            'quote': quote,
            'crypto': json.loads(crypto_request.content)
        }
        return render(request, 'pages/prices.html', context)
    else:
        return render(request, 'pages/prices.html', {})
