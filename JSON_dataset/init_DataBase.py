import json
import csv

from tqdm import tqdm

from recensione import *
import re
import Sentiment_analyzer as Sa


def start(file_path, lista):
    """
    Carica il file JSON su python riga per riga, e viene aggiunta in una lista temporanea
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
    '''
    Dato un ASIN (codice univoco dei prodotti amazon ) ritorna il nome del prodotto
    :param asin: asin da convertire
    :param lista: lista dei dati dei prodotti
    :return:
    '''
    for elemento in lista:

        if elemento["asin"] == asin:
            return elemento["title"]


class counter:
    '''
     counter globale
    '''
    def __init__(self, valore):
        self.value = valore

    def increment(self):
        self.value = self.value + 1

    def value_of(self):
        return f"{self.value}"


def init_datasetcsv(nome_categoria, lista_iterare, meta_lista_iterare, cont):
    '''
    data una lista di recensioni , una lista di prodotti e un contatore
    si occupa di mettere tutto insieme filtrando i dati inutile creando un CSV ready to use
    :param nome_categoria: nome della categoria di amazon
    :param lista_iterare:  lista delle recensioni
    :param meta_lista_iterare: lista con i dettagli dei prodotti   (asin e title)
    :param cont:  contatore globale, per mantenere
    :return:
    '''
    Analizzatore = Sa.Sentiment_analyzers()

    for obj in tqdm(lista_iterare):
        try:
            title = asin_to_title(obj["asin"], meta_lista_iterare)

            if title is None:
                continue

            if len(obj["reviewText"].replace('\n', ' ')) <= 20:
                continue

            if re.search("<span .*", title):
                continue

            cleaned_review_text = obj["reviewText"].replace('\n', ' ')

            if len(cleaned_review_text) > 500:
                continue

            temp = recensione(cont.value_of(),
                              obj["reviewerName"].replace('\n', ' '),
                              cleaned_review_text,
                              obj["asin"],
                              title,
                              nome_categoria,
                              Analizzatore.Analizza_Vader(cleaned_review_text),
                              Analizzatore.Analizza_Distilroberta(cleaned_review_text),
                              Analizzatore.Anilizza_Textblob(cleaned_review_text)
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

stream = open("dataset_sentiment.csv", "w", newline='')
writer = csv.writer(stream)
header = ['pk',
          'reviewerName',
          'reviewText',
          'asin',
          'title',
          'categoria',
          'vader_valore_negativo',
          'vader_valore_neutrale',
          'vader_valore_positivo',
          'vader_valore_compound',
          'distilroberta_sentimento',
          'distilroberta_sentimento_valore',
          'textblob_valore_positivo',
          'textblob_valore_compound'
          ]
writer.writerow(header)
print("ci sto provando")
init_datasetcsv("Cd e Vynil", musiclist, meta_musiclist, count)
init_datasetcsv("Movies and TV", movielist, meta_movielist, count)

stream.close()
