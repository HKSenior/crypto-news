from datetime import datetime

from django.shortcuts import render
from decouple import config
from pytz import timezone

from . models import News


def news(request):
    # Get articles from db
    records = News.objects.all().order_by('-news_id')

    context = {
        'news': list(records),
        'now': datetime.now(tz=timezone(config('CELERY_TIMEZONE')))
    }

    print(context)
    return render(request, 'pages/news.html', context)
