from Searcher import *
from Results import *
from Indexing.Database import Database as data
from Indexing.indexing import Indexer


is_index_dir = open_dir('../Indexing/indexdir_2.0')

if not is_index_dir:
    db = data.Database('../JSON_dataset/dataset_sentiment.csv')
    db.init_DB()

    index = Indexer(db)
    index.create_index()

    if index.ix.is_empty() == True:
        print("fallimento")


"""
ho commentato per rendere la fase di testing più veloce senza dover fare sempre input
"""
# query= input("Inserire query: ")
# sentiment_analyzer =input("Inserire analizzatore sentimento: ")
# sentiment=input("Inserire sentimento: ")

search= Index_Searcher()
search.inizializza()

query="segment"
results= search.submit_query(query,results_threshold=100,ricerca_precisa=False)



""""
test per vedere se funziona searcher
"""
# print("eseguo test")
# search.Test_Controllo_Index("segment")

