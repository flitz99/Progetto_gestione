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

start('review_testing.json', musiclist)
start('meta_review.json', meta_musiclist)

contatore = 1

stream = open("music.csv", "w" , newline='')
writer = csv.writer(stream)
header = ['pk', 'reviewerName', 'reviewText', 'asin', 'title', 'categoria']
writer.writerow(header)

for music in musiclist:
    try:

        title = asin_to_title(music["asin"], meta_musiclist)

        if re.search("<span .*", title):
            continue

        temp = recensione(contatore,
                          music["reviewerName"].replace('\n', ' '),
                          music["reviewText"].replace('\n', ' '),
                          music["asin"],
                          title,
                          "Cd's Vynil"
                          )
        writer.writerow(temp)

        contatore = contatore + 1

    except KeyError:
        continue

stream.close()
