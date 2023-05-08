from Searcher import *
from Results import *
from Indexing_Database.Crea_index import *

"""
ho commentato per rendere la fase di testing più veloce senza dover fare sempre input
"""

starter = Start_indexing()



# query= input("Inserire query: ")
sentiment_analyzer = input("Inserire analizzatore sentimento: ")

if sentiment_analyzer == "Vader" or sentiment_analyzer == "TextBlob":
    print("positivo , negativo o neutrale ?")
    sentiment = input("Inserire sentimento: ")
elif sentiment_analyzer == "distilroberta":
    print("joy, ")
    sentiment = input("Inserire tipo sentimento: ")

query = "good reads"
results = search.submit_query(query, results_threshold=5, ricerca_precisa=False)

for cont, r in enumerate(results):
    print(cont, r)

""""
test per vedere se funziona searcher
"""
# print("eseguo test")
# search.Test_Controllo_Index("segment")
