import csv
from JSON_dataset import recensione as rec


class Database:

    def __init__(self, csv_file):

        self.file_name = csv_file
        self.csv_reader = csv.reader(open(self.file_name), delimiter=",")  # ogni field é separato da una ','

        self.lista_recensioni = []  # lista

    def init_DB(self):

        for index, riga in enumerate(self.csv_reader):  # enumerate, serve per avere un contatore del elemento attuale

            if index == 0:  # salto header perchè non necessario
                continue

            else:  # index>0 quindi sono nei records
                temp = []  # lista temporanea per avere i vari campi del record
                for elemento_estratto in riga:
                    temp.append(elemento_estratto)

                self.lista_recensioni.append(temp)  # aggiungo la recensione alla lista

    def Test_numero_ultima_recensione(self):
        temp = self.lista_recensioni[-1]
        print(temp.get_pk())  # controllo pk del ultimo elemento nella lista

    def Test_Conta_caratteri_totali(self, lista):

        for l in self.lista_recensioni:
            temp = l
            lista.append(temp.count_review())

    def Benchmark_mode(self):
        print("procedo a prendere 100 recensioni in modo casuale")
        import random
        #solo_film = filter(lambda l: l[5] == 'Movies and TV', self.lista_recensioni)
        solo_film = [l for l in self.lista_recensioni if l[5] == 'Movies and TV']

        updatedlist = random.sample(solo_film, 100)

        self.lista_recensioni = updatedlist
