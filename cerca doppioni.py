#una volta scaricata la lista di tutti i film tramite le API moviedb, parecchi di essi hanno il nome ripetuto
#con questo script risolvo il problema, per i film dal nome ripetuto aggiungo l'anno di produzione
#incompleto, ci sono alcuni film The Princess (2022) usciti lo stesso anno, altri film non hanno un anno di produzione

import pandas as pd
pd.set_option('display.width', 4000)
pd.set_option('display.max_columns', 100)
import numpy as np

df=pd.read_csv('../movies_dataset.csv')


def cambia_titolo(index, oldtitle):
    elementi = df[df['title'] == oldtitle]
    #print(elementi.shape[0])
    for idx, row in elementi.iterrows():
        newtitle = oldtitle + " (" + row['release_date'][:7] + ")"
        print(newtitle)
        #print(df.loc[index, 'title'])
        df.loc[idx, 'title'] = newtitle

def cancella_doppioni():
    for index, row in df.iterrows():
        title = row['title']

        rows = df[df['title'] == title]
        if(rows.shape[0]) > 1:
            print(title)
            cambia_titolo(index, title)

def cerca_doppioni(titolo):
    row = df[df['title'] == titolo]
    print(row)
    print(row.shape[0])

#cerca_doppioni("Verdi: Macbeth")
cancella_doppioni()
df.to_csv('../movies_dataset.csv')
