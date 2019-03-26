from datetime import datetime

from pytz import timezone
from decouple import config
from django.shortcuts import render

from . models import News


def news(request):
    # Get articles from db
    records = News.objects.all().order_by('-news_id')

    context = {
        'news': list(records),
        'now': datetime.now(tz=timezone(config['CELERY_TIMEZONE'])),
        'hello': 'Hello, World!!!'
    }

    print(context)
    return render(request, 'pages/news.html', context)
