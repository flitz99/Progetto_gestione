import os
from Database import Database
from Indexing import Indexer

def crea_index_se_non_esiste():
    is_index_dir = os.path.exists('../Indexing/indexdir_2.0')

    if not is_index_dir:
        db = Database('../JSON_dataset/dataset_sentiment.csv')
        db.init_DB()

        index = Indexer(db)
        index.create_index()

        if index.ix.is_empty() == True:
            print("fallimento")


