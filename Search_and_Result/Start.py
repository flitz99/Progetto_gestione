from Searcher import *
from Results import *
from Indexing_Database.Crea_index import *

"""
ho commentato per rendere la fase di testing più veloce senza dover fare sempre input
"""

starter = Start_indexing()

#Richiesta e ricerca query inserita nell'index
query= input("Inserire query: ")
print("vuoi usare BM25F o TF_IDF? (scelta omessa o errata viene usato TF_IDF come standard)")
scoring_method=input("Inserire meccanismo di scoring: ")
search = Index_Searcher(algoritmo_di_ricerca=scoring_method)


results = search.submit_query(query, results_threshold=5, ricerca_precisa=False) #Ricerca query nell'index

#Risultati prima della sentiment
for cont, r in enumerate(results):
    print(cont, r)


#richiesta analizzatore sentiment
sentiment_analyzer = input("Inserire analizzatore sentimento: ")

if sentiment_analyzer == "Vader" or sentiment_analyzer == "TextBlob":
    print("positivo , negativo o neutrale ?")
    sentiment = input("Inserire sentimento: ")
elif sentiment_analyzer == "distilroberta":
    print("joy, surprise, neutral, fear, sadness, anger, disgust? ")
    sentiment = input("Inserire tipo sentimento: ")

#Risultati dopo sentiment
#for cont, r in enumerate(results):
#    print(cont, r)

""""
test per vedere se funziona searcher
"""
# print("eseguo test")
# search.Test_Controllo_Index("segment")
