from django.db import models


class News(models.Model):
    news_id = models.IntegerField()
    imageurl = models.TextField()
    source = models.CharField(max_length=50)
    url = models.TextField()
    title = models.TextField()
    categories = models.TextField()

    def __str__(self):
        return self.title
