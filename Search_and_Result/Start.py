from Searcher import *
from Results import *
from Indexing_Database.Crea_index import *


"""
ho commentato per rendere la fase di testing più veloce senza dover fare sempre input
"""


# query= input("Inserire query: ")
# sentiment_analyzer = input("Inserire analizzatore sentimento: ")
# sentiment=input("Inserire sentimento: ")

starter = Start_indexing()

search= Index_Searcher()
search.inizializza()

query="segment"
results= search.submit_query(query,results_threshold=100,ricerca_precisa=False)



""""
test per vedere se funziona searcher
"""
# print("eseguo test")
# search.Test_Controllo_Index("segment")

