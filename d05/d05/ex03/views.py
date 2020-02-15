from django.shortcuts import render
from ex03.models import Movies


def populate(request):
    try:
        Movies(episode_nb=1, title='The Phantom Menace', director='George Lucas',\
            producer='Rick McCallum', release_date='1999-05-19').save()
        Movies(episode_nb=2, title='Attack of the Clones', director='George Lucas',\
            producer='Rick McCallum', release_date='2002-05-16').save()
        Movies(episode_nb=3, title='Revenge of the Sith', director='George Lucas',\
            producer='Rick McCallum', release_date='2005-05-19').save()
        Movies(episode_nb=4, title='A New Hope', director='George Lucas',\
            producer='Gary Kurtz, Rick McCallum', release_date='1977-05-25').save()
        Movies(episode_nb=5, title='The Empire Strikes Back', director='Irvin Kershner',\
            producer='Gary Kutz, Rick McCallum', release_date='1980-05-17').save()
        Movies(episode_nb=6, title='Return of the Jedi', director='Richard Marquand',\
            producer='Howard G. Kazanjian, George Lucas, Rick McCallum', release_date='1983-05-25').save()
        Movies(episode_nb=7, title='The Force Awakens', director='J. J. Abrams',\
            producer='Kathleen Kennedy, J. J. Abrams, Bryan Burk', release_date='2015-12-11').save()
        result = 'OK'
    except Exception as error:
        print(f'\033[91m Error: {error} \033[91m')
        result = str(error)
    return render(request, 'ex03/populate.html', {'result': result})


def display(request):
    movies_list = []
    try:
        for movie in Movies.objects.all():
            movies_list.append([movie.episode_nb, movie.title, movie.producer, movie.director, movie.opening_crawl, movie.release_date])
    except:
        movies_list = []
    return render(request, 'ex03/display.html', {'movies_list': movies_list, 'is_empty': len(movies_list) == 0 })

