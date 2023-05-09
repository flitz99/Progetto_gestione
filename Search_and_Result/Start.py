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
scoring_method = input("Inserire meccanismo di scoring: ")

search = Index_Searcher(algoritmo_di_ricerca=scoring_method)
relevant_results = search.submit_query(query, results_threshold=25, ricerca_precisa=False)  # Ricerca query nell'index

#Risultati prima della sentiment
for cont, r in enumerate(relevant_results):
    print(cont, r)


#richiesta analizzatore sentiment
sentiment_analyzer = input("Inserire analizzatore sentimento: ")

if sentiment_analyzer == "Vader":
    print("positivo , negativo o neutrale ?")
    sentiment = input("Inserire sentimento: ")
elif sentiment_analyzer == "TextBlob":
    print("positivo o negativo ?")
    sentiment = input("Inserire sentimento: ")
elif sentiment_analyzer == "distilroberta":
    print("joy, surprise, neutral, fear, sadness, anger, disgust? ")
    sentiment = input("Inserire tipo sentimento: ")


results = Results(sentiment_analyzer, sentiment, relevant_results)
sent_ord_results = results.generate_results()

results.print_results_txt(sent_ord_results,'console')
results.print_results_txt(sent_ord_results,'txt')



