from __future__ import absolute_import, unicode_literals
from celery import shared_task

import psycopg2
import requests
import json
from pytz import timezone
from string import Template
from decouple import config
from datetime import datetime


@shared_task()
def update_news():
    try:
        # Connect to database and create cursor
        connection = psycopg2.connect(
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            database=config('DB_NAME'),
            port="5432"
        )
        cursor = connection.cursor()

        # Get news data
        data_requests = requests.get(
            "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        )
        data = json.loads(data_requests.content)

        # Get the latest news articles id from the db
        template = Template("SELECT news_id "
                            "FROM $table "
                            "ORDER BY news_id DESC LIMIT 1;")
        cursor.execute(template.substitute(table=config('DB_TABLE')))
        latest_db_news_id = cursor.fetchone()[0]

        # Compare the db id with the latest id requested
        requested_id = int(data['Data'][0]['id'])
        if latest_db_news_id == requested_id:
            # No new articles to add to the db
            pass
        elif requested_id > latest_db_news_id:
            # We have new articles to add to the db
            print()

            # Insert query template
            template = Template(
                "INSERT INTO $table "
                "(news_id, imageurl, source, "
                "url, title, categories, when_added) "
                "VALUES ($news_id, '$imageurl', "
                "'$source', '$url', $title, '$categories', "
                "TIMESTAMP '$when_added');"
            )            

            # Add the new articles
            for item in data['Data']:
                if int(item['id']) > latest_db_news_id:
                    query = template.substitute(
                        table=config('DB_TABLE'),
                        news_id=int(item['id']),
                        imageurl=item['imageurl'],
                        source=item['source'],
                        url=item['url'],
                        title='$$' + item['title'] + '$$',
                        categories=item['categories'],
                        when_added=datetime.now(tz=timezone('US/Eastern'))
                    )
                    cursor.execute(query)
                    connection.commit()                    

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL\n\t", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
