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

                review = rec.recensione(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5])  # creo una recensione
                self.lista_recensioni.append(review)  # aggiungo la recensione alla lista

    def Test(self):
        temp = self.lista_recensioni[-1]
        print(temp.get_pk())  # controllo pk del ultimo elemento nella lista



'''
db = Database('../JSON_dataset/dataset.csv')
db.init_DB()
db.Test()
'''
