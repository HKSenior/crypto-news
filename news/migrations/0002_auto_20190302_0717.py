# Generated by Django 2.1.7 on 2019-03-02 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_id',
            field=models.IntegerField(),
        ),
    ]
