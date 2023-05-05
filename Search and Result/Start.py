from Src.Searcher import Index_Searcher
from Src.Results import Results
#Inserimenti da parte dell'utente
query= input("Inserire query: ")
sentiment_analyzer =input("Inserire analizzatore sentimento: ")
sentiment=input("Inserire sentimento: ")

search= Index_Searcher()
search.inizializza()

results= search.submit_query(query,results_threshold=100,expand=True)
res= Results("Vader",sentiment,results,ranking_fun="balanced_weighted_avg")




