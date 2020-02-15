from django.shortcuts import render
from ex04.models import Movies
from django.shortcuts import get_object_or_404
import psycopg2
from psycopg2 import sql


def init(request):
    result = 'OK'
    create_table ="""
        CREATE TABLE IF NOT EXISTS ex04_movies (
            episode_nb integer PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        )
        """
    try:
        conn = psycopg2.connect(database='formationdjango', user='djangouser', \
            password='secret', host='localhost', port='5432')
        cur = conn.cursor()
        
        cur.execute(create_table)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        result = str(error)
    return render(request, 'ex04/init.html', {'result': result})


def populate(request):
    my_movies = [
    {'episode_nb': 1, 'title': 'The Phantom Menace', 'opening_crawl': ' ', 'director': 'George Lucas',\
            'producer': 'Rick McCallum', 'release_date': '1999-05-19'},\
    {'episode_nb': 2, 'title': 'Attack of the Clones', 'opening_crawl': ' ', 'director': 'George Lucas',\
            'producer': 'Rick McCallum', 'release_date': '2002-05-16'},\
    {'episode_nb': 3, 'title': 'Revenge of the Sith', 'opening_crawl': ' ', 'director': 'George Lucas',\
            'producer': 'Rick McCallum', 'release_date': '2005-05-19'},
    {'episode_nb': 4, 'title': 'A New Hope', 'opening_crawl': ' ', 'director': 'George Lucas',\
            'producer': 'Gary Kurtz, Rick McCallum', 'release_date': '1977-05-25'},\
    {'episode_nb': 5, 'title': 'The Empire Strikes Back', 'opening_crawl': ' ', 'director': 'Irvin Kershner',\
            'producer': 'Gary Kutz, Rick McCallum', 'release_date': '1980-05-17'},\
    {'episode_nb': 6, 'title': 'Return of the Jedi', 'opening_crawl': ' ', 'director': 'Richard Marquand',\
            'producer': 'Howard G. Kazanjian, George Lucas, Rick McCallum', 'release_date': '1983-05-25'},\
    {'episode_nb': 7, 'title': 'The Force Awakens', 'opening_crawl': ' ', 'director': 'J. J. Abrams',\
            'producer': 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', 'release_date': '2015-12-11'}
    ]
    result = ''
    try:
        conn = psycopg2.connect(database='formationdjango', user='djangouser', \
            password='secret', host='localhost', port='5432')
        conn.autocommit = True
        cur = conn.cursor()
        for m in my_movies:
            values = [m['episode_nb'], m['title'], m['opening_crawl'], m['director'], m['producer'], m['release_date']]
            insert = sql.SQL('INSERT INTO ex04_movies (episode_nb, title, opening_crawl ,director, producer, release_date) VALUES ({})').\
                format(sql.SQL(',').join(map(sql.Literal, values)))
            cur.execute(insert)
            conn.commit()
            result += 'OK: ' + m['title'] + '\n\n'
    except Exception as error:
        print(f'\033[91m Error: {error} \033[91m')
        result += str(error) + '\n'
    return render(request, 'ex04/populate.html', {'result': result})


def display(request):
    try:
        conn = psycopg2.connect(database='formationdjango', user='djangouser', \
            password='secret', host='localhost', port='5432')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex04_movies")
        movies_list = cur.fetchall()
        print(cur.fetchall())
    except Exception as error:
        is_empty = 1
        print(error)
    return render(request, 'ex04/display.html', {'movies_list': movies_list, 'is_empty': 0})


def remove(request):
    movies_titles = []
    try:
        conn = psycopg2.connect(database='formationdjango', user='djangouser', \
            password='secret', host='localhost', port='5432')
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex04_movies")
        movies = cur.fetchall()
        for m in movies:
            movies_titles.append(m[1])
        print(movies_titles)
        movie_to_delete = request.POST.get('movie_to_delete', "")
        delete_sql = "DELETE from ex04_movies WHERE title = %s"
        cur.execute(delete_sql, (movie_to_delete,))
        conn.commit()
        result = 'OK'
    except Exception as e:
        print(e)
        result = str(e)
    return render(request, 'ex04/remove.html', {'movies_titles': movies_titles, 'result': result})