#con questo script recupero una lista di film con le API di moviedb
import requests
import pandas as pd
import sys
import threading, logging
api_key = ""
language_count = {
    'en':10000,
    'it':5000
}


def get_movies(lang, freq):
    url = 'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&with_original_language={lang}'.format(
        api_key=api_key, lang=lang)
    # print(url)
    movies = []
    page = 1
    progress = 0
    while movies.__len__() < freq:
        try:
            res = requests.get(url + "&page=" + str(page))
        except:
            raise ('not connected to internet or movidb issue')

        if res.status_code != 200:
            print('error')
            return []

        res = res.json()

        if 'errors' in res.keys():
            print('api error !!!')
            return movies

        movies = movies + res['results']

        if progress != round(len(movies) / freq * 100):
            progress = round(len(movies) / freq * 100)
            if progress % 5 == 0:
                print(progress, end="%, ")

        page = page + 1
        # break
        # print(res)
    return movies

all_movies = []

for key in language_count:
  # print(key,language_count[key])
  print("Downloading ", key, end=" : ")
  movies = get_movies(key,language_count[key])
  all_movies = all_movies + movies
  print('Total movies found : ', movies.__len__())
  # break

df = pd.DataFrame(all_movies, columns=['genre_ids', 'id', 'original_language',
       'overview', 'popularity', 'release_date', 'title', 'vote_average', 'vote_count'])
df.to_csv('../movies_list.csv', index=False)


