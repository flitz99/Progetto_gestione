import os
from Indexing_Database import Database as datab
from Indexing_Database import Indexing as indx
class Start_indexing:

    def __init__(self):
        print("controllo se Index Esiste")
        self.crea_index_se_non_esiste()

    def crea_index_se_non_esiste(self):
        is_index_dir = os.path.exists('/indexdir_2.0')

        if not is_index_dir:
            print("index non esiste attendere la sua creazione")
            db = datab.Database('../JSON_dataset/dataset_sentiment.csv')
            db.init_DB()

            index = indx.Indexer(db)
            index.create_index()

            if index.ix.is_empty() == True:
                print("fallimento")

        else:
            print("index esiste , Ready to go!")