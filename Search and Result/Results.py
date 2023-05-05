
class Results:
        #Costruisce la struttura dati dei risultati ottenuti da una query
        #Incrocia punteggio di pertinenza con quello della sentiment analysis

        def __init__(self,tool_name,sentiment,results, textual_field = "text",ranking_fun = "balanced_weighted_avg"):

            self.sentiment_tool=tool_name
            self.results = self.generate_results(results,"field")
            self.ordered_results=None

        def generate_results(self, results,textual_field):
                #Costruisco struttura dati dei risultati
                #Uso come struttura dati una lista di dizionari e prendo sentiment analysis del relativo tool
        
                if not results:
                    raise Exception("Nessun risultato per questa query")

                self.ordered_results=[]

                for hit in results:
                    result=dict()
                    # Aggiunge numero di indice del documento
                    result["docnum"]=hit.docnum
                    # Aggiunge tutti i campi indicizzati del documento
                    result.update(dict(hit))
                    #Aggiunge score del documento
                    result["pert_score"]=hit.score
                    #Aggiunge valore sentiment
                    result["sent_score"]=hit.sentiment_score

                    self.ordered_results.append(result)

                return "prova"



        #Controllo che tool di sentiment inserito sia corretto
        def check_sentiment(tool_name):
            if tool_name == "Vader" or tool_name=="Roberta":
                return True
            return False