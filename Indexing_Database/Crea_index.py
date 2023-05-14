import os
from Indexing_Database import Database as DATAB
from Indexing_Database import Indexing as INDX
class Start_indexing:

    def __init__(self):
        print("controllo se Index Esiste")
        self.crea_index_se_non_esiste()

    def crea_index_se_non_esiste(self):
        is_index_dir = os.path.exists('../Search_and_Result/indexdir_2.0')

        if not is_index_dir:
            print("index non esiste attendere la sua creazione")
            db = DATAB.Database('../JSON_dataset/dataset_sentiment.csv')
            db.init_DB()

            index = INDX.Indexer(db)
            index.create_index()

            if index.ix.is_empty() == True:
                print("fallimento")

        else:
            print("index esiste , Ready to go!")
