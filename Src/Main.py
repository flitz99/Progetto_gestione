from Search.Searcher import Index_Searcher

#Inserimenti da parte dell'utente
query= input("Inserire query: ")
sentiment_analyzer =input("Inserire analizzatore sentimento: ")
sentiment=input("Inserire sentimento: ")

search= Index_Searcher()
search.inizializza()

results= search.submit_query(query,results_threshold=100,expand=True)




