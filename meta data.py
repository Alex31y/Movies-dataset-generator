import requests
import pandas as pd
import sys
import threading, logging

df = pd.read_csv('../movies_dataset.csv')
ids = df['id'].tolist()
api_key = ""


def get_cast(id):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'.format(api_key=api_key, movie_id=id)
    #print(url)
    try:
        res = requests.get(url)
    except:
        raise ('not connected to internet or movidb issue')

    if res.status_code != 200:
        print('error')
        return

    res = res.json()

    if 'errors' in res.keys():
        print('api error !!!')
        return credits
    # print(res)

    cast = res['cast']
    df = pd.DataFrame(cast)
    if 'popularity' in df.columns:
        df = df.sort_values('popularity', ascending=False)
    if 'name' in df.columns:
        df = df['name']
    else:
        return
    df = df.head(5) #prendo solo i primi 5 attori per popolarità

    director = res['crew']
    dir = pd.DataFrame(director)
    if 'job' in dir.columns:
        dir = dir.loc[dir['job'] == 'Director']
    else:
        return
    dir = dir['name']

    credits = df.tolist()
    dir = dir.tolist()
    return credits, dir

def get_keyword(id):
    url = 'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key={api_key}'.format(api_key=api_key,movie_id=id)
    #print(url)
    try:
        res = requests.get(url)
    except:
        raise ('not connected to internet or movidb issue')

    if res.status_code != 200:
        print('error')
        return []

    res = res.json()

    if 'errors' in res.keys():
        print('api error !!!')
        return credits
    # print(res)

    word = res['keywords']
    df = pd.DataFrame(word)
    if 'name' in df.columns:
        df = df['name']
    else:
        return

    keywords = df.tolist()
    return keywords

i = 0
import concurrent.futures

def process_movie(id):
    credits, dir = get_cast(id)
    keywords = get_keyword(id)
    row = {'id': id, 'director': dir, 'cast': credits, 'keywords' : keywords}
    return row

df = pd.DataFrame(columns=['id', 'director', 'cast', 'keywords'])
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(process_movie, id) for id in ids]
    for future in concurrent.futures.as_completed(futures):
        try:
            row = future.result()
            df.loc[len(df)] = row
            i+=1
            print(i)
        except Exception as e:
            print(e)

df.to_csv("../metadata.csv")





