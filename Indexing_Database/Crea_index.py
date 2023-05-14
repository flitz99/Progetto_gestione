import os
from Indexing_Database import Database as datab
from Indexing_Database import Indexing as indx
class Start_indexing:

    def __init__(self):
        print("Controllo se Index Esiste...")
        self.crea_index_se_non_esiste()

    def crea_index_se_non_esiste(self):
        is_index_dir = os.path.exists('../Search_and_Result/indexdir_2.0')

        if not is_index_dir:
            print("Index non esistente,  attendere la sua creazione... \n")
            db = datab.Database('../JSON_dataset/dataset_sentiment.csv')
            db.init_DB()

            index = indx.Indexer(db)
            index.create_index()

            if index.ix.is_empty() == True:
                print("fallimento")

        else:
            print("L'index esiste, Ready to go! \n")
