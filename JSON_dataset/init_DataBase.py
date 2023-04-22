import json
import csv
from recensione import *
import re


def start(file_path, lista):
    """
    :param file_path:  path del file json da leggere
    :param lista:  lista vuota che verra riempita con gli oggetti letti dal file json
    :return: none, riempe la lista per reference
    """

    print(f"{file_path} insieme alla {lista} ")
    with open(file_path) as file:
        for jsonObj in file:

            temp = json.loads(jsonObj)
            lista.append(temp)


def asin_to_title(asin, lista):
    for elemento in lista:

        if elemento["asin"] == asin:
            return elemento["title"]


musiclist = []
meta_musiclist = []

movielist = []
meta_movielist = []

start('CDs_and_Vinyl_25k.json', musiclist)
start('meta_CDs_and_Vinyl_50k.json', meta_musiclist)

start('Movies_and_TV_25k.json', movielist)
start('meta_Movies_and_TV_50k.json', meta_movielist)

contatore = 1

stream = open("dataset.csv", "w", newline='')
writer = csv.writer(stream)
header = ['pk', 'reviewerName', 'reviewText', 'asin', 'title', 'categoria']
writer.writerow(header)

'''
itero la lista dei Tv e Movies e lo aggiungo al dataset
'''

for music in musiclist:
    try:
        print(contatore)
        title = asin_to_title(music["asin"], meta_musiclist)

        if title is None:
            continue

        if   len(music["reviewText"].replace('\n', ' ')) <= 20:
            continue

        if re.search("<span .*", title):
            continue

        temp = recensione(contatore,
                          music["reviewerName"].replace('\n', ' '),
                          music["reviewText"].replace('\n', ' '),
                          music["asin"],
                          title,
                          "Cd's Vinyl"
                          )
        writer.writerow(temp)

        contatore = contatore + 1

    except KeyError:
        continue

'''
itero la lista dei Tv e Movies e lo untagging al dataset
'''

for movie in movielist:
    try:
        print(contatore)
        title = asin_to_title(movie["asin"], meta_movielist)

        if title is None:
            continue

        if   len(movie["reviewText"].replace('\n', ' ')) <= 20:
            continue

        if re.search("<span .*", title):
            continue

        temp = recensione(contatore,
                          movie["reviewerName"].replace('\n', ' '),
                          movie["reviewText"].replace('\n', ' '),
                          movie["asin"],
                          title,
                          "Movies and Tv"
                          )
        writer.writerow(temp)

        contatore = contatore + 1

    except KeyError:
        continue

stream.close()
