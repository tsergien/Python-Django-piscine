from django.shortcuts import render
import psycopg2


def init(request):
    commands = ([
        """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb integer PRIMARY KEY,
            opening_crawl VARCHAR,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        )
        """])
    result = 'OK'
    try:
        conn = psycopg2.connect(database='formationdjango', user='djangouser', \
            password='secret', host='localhost', port='5432')
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        result = error
    return render(request, 'ex00/init.html', {'result': result})

