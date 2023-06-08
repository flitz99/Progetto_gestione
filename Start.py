from Search_and_Result.Searcher import *
from Search_and_Result.Results import *
from Indexing_Database.Crea_index import *

'''
funzione che crea index se non esiste ci mette 2-3 minuti
'''
starter = Start_indexing()

# Richiesta e ricerca query inserita nell'index
query = input("Inserire query: ")
print("Vuoi usare BM25F o TF_IDF? (In caso di scelta omessa o errata si utilizza TF_IDF come standard)")
scoring_method = input("Inserire meccanismo di scoring: ")

search = Index_Searcher(algoritmo_di_ricerca=scoring_method )
relevant_results = search.submit_query(query, results_threshold=100, ricerca_precisa=False)  # Ricerca query nell'index

#Se ho risultati
if relevant_results:
    # richiesta analizzatore sentiment
    print("Vuoi usare Vader, TextBlob o distilroberta? (In caso di scelta omessa o errata si utilizza Vader positivo come standard)")
    sentiment_analyzer = input("Inserire sentiment analyzer: ")
    if sentiment_analyzer == "Vader":
        print("positivo , negativo o neutrale ?")
        sentiment = input("Inserire tipo di sentimento: ")
    elif sentiment_analyzer == "TextBlob":
        print("positivo o negativo ?")
        sentiment = input("Inserire tipo di sentimento: ")
    elif sentiment_analyzer == "distilroberta":
        print("joy, surprise, neutral, fear, sadness, anger, disgust? ")
        sentiment = input("Inserire tipo di sentimento: ")
    else: #Default
        sentiment_analyzer="Vader"
        sentiment="positivo"
        print("Hai scelto di usare Vader Positivo")
    print("\n \n")

    results = Results(sentiment_analyzer, sentiment, relevant_results)
    sent_ord_results = results.generate_results()

    results.print_results_txt(sent_ord_results,'console',limit=10)
    results.print_results_txt(sent_ord_results,'txt')

