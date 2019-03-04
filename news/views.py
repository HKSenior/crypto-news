from django.shortcuts import render

from . models import News


def news(request):
    # Get articles from db
    records = News.objects.all()

    context = {                
        'news': list(records)
    }
    return render(request, 'pages/news.html', context)
