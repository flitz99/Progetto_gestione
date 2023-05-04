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


class counter:

    def __init__(self, valore):
        self.value = valore

    def increment(self):
        self.value = self.value + 1

    def value_of(self):
        return f"{self.value}"


def init_datasetcsv(nome_categoria, lista_iterare, meta_lista_iterare, cont):
    for obj in lista_iterare:
        try:
            print(cont.value_of())
            title = asin_to_title(obj["asin"], meta_lista_iterare)

            if title is None:
                continue

            if len(obj["reviewText"].replace('\n', ' ')) <= 20:
                continue

            if re.search("<span .*", title):
                continue

            temp = recensione(cont.value_of(),
                              obj["reviewerName"].replace('\n', ' '),
                              obj["reviewText"].replace('\n', ' '),
                              obj["asin"],
                              title,
                              nome_categoria
                              )
            writer.writerow(temp)

            cont.increment()

        except KeyError:
            continue





musiclist = []
meta_musiclist = []

movielist = []
meta_movielist = []

count = counter(1)

start('CDs_and_Vinyl_25k.json', musiclist)
start('meta_CDs_and_Vinyl_50k.json', meta_musiclist)

start('Movies_and_TV_25k.json', movielist)
start('meta_Movies_and_TV_50k.json', meta_movielist)

stream = open("dataset.csv", "w", newline='')
writer = csv.writer(stream)
header = ['pk', 'reviewerName', 'reviewText', 'asin', 'title', 'categoria']
writer.writerow(header)

init_datasetcsv("Cd e Vynil", musiclist, meta_musiclist, count)
init_datasetcsv("Movies and TV", movielist, meta_movielist, count)

stream.close()

