import os
import Database
import Indexing

def crea_index_se_non_esiste():
    is_index_dir = os.path.exists('../Indexing/indexdir_2.0')

    if not is_index_dir:
        db = Database.Database('../JSON_dataset/dataset_sentiment.csv')
        db.init_DB()

        index = Indexing.Indexer(db)
        index.create_index()

        if index.ix.is_empty() == True:
            print("fallimento")


crea_index_se_non_esiste()