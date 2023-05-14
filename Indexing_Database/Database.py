import csv
from JSON_dataset import recensione as rec
import random

class Database:
    '''
    Classe che gestisce il caricamento dei dati da file CSV dentro python
    '''

    def __init__(self, csv_file):

        self.file_name = csv_file
        self.csv_reader = csv.reader(open(self.file_name), delimiter=",")  # ogni field é separato da una ','

        self.lista_recensioni = []  # lista

    def init_DB(self):
        '''
        carica il file CSV sepcificato alla inizializzazione e lo trasforma in una lista di dati dentro un altra lista
        :return:
        '''

        for index, riga in enumerate(self.csv_reader):  # enumerate, serve per avere un contatore del elemento attuale

            if index == 0:  # salto header perchè non necessario
                continue

            else:  # index>0 quindi sono nei records
                temp = []  # lista temporanea per avere i vari campi del record
                for elemento_estratto in riga:
                    temp.append(elemento_estratto)

                self.lista_recensioni.append(temp)  # aggiungo la recensione alla lista

    def Test_numero_ultima_recensione(self):
        '''
        Piccolo test per vedere quante recensioni ci sono
        :return:
        '''
        temp = self.lista_recensioni[-1]
        print(temp.get_pk())  # controllo pk del ultimo elemento nella lista

    def Test_Conta_caratteri_totali(self, lista):
        '''
        Piccolo test usato per valutare se potessimo usare open AI come sentiment analyzer
        calcoliamo la lunghezza totale dei caratteri di tutte le recensioni

        OPEN-AI accetta
        :param lista: sono tutte le recensioni
        :return: ritorna il colcolo
        '''

        for l in self.lista_recensioni:
            temp = l
            lista.append(temp.count_review())

    def Benchmark_mode(self):
        '''
        per il benchmark filtriamo la lista  e prendiamo solamente 100 recensioni di film
        :return: nullo
        '''
        print("procedo a prendere 100 recensioni in modo casuale")

        solo_film = [l for l in self.lista_recensioni if l[5] == 'Movies and TV']
        if len(solo_film) >= 100:
            updatedlist = random.sample(solo_film, 100)
            self.lista_recensioni = updatedlist
        else:
            print("elementi non bastano")
