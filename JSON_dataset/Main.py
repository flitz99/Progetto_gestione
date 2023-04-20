import json
import csv
from recensione import *

def start(file_path, lista):
    '''
    :param file_path:  path del file json da leggere
    :param lista:  lista vuota che verra riempita con gli oggetti letti dal file json
    :return: none, riempe la lista per reference
    '''

    print(f"{file_path} insieme alla {lista} ")
    with open(file_path) as file:
        for jsonObj in file:
            temp = json.loads(jsonObj)
            lista.append(temp)


def asin_to_title(asin, lista):
    for elemento in lista:

        if elemento["asin"] == asin:
            return elemento["title"] , elemento["main_cat"]


musiclist = []
meta_musiclist = []
start('review_testing.json', musiclist)
start('meta_review.json', meta_musiclist)

musiclist= musiclist[0:100]
'''

f = csv.writer(open("test.csv", "wb+"))
f.writerow(["pk", "reviewerName", "reviewText", "asin", "title", "main_cat"])
'''


contatore = 0
for music in musiclist:

    try:

        lista_risultato = asin_to_title(music["asin"], meta_musiclist)

        print(lista_risultato[0])
        print(f"Cd's and vinyl")
        print("******************************************************")

    except KeyError:
        continue
