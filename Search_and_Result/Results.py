

class Results:
    '''
         ingresso risultati , analizzatore  , sentimento_passato
         - riordinare
         - filtraggio selettivo
         - ranking function -> ordina i risultati in base alla combinazione
                                punteggio di pertinenza + punteggio di sentiment
        uscita lista oridnata
    '''
    def __init__(self,tool_name,sentiment,results,ranking_fun = "balanced_weighted_avg"):

            self.sentiment_tool=tool_name
            self.sentiment=sentiment
            self.raw_results = results
            self.results= None



    def generate_results(self):

        self.results=[]

        if self.sentiment_tool=="distilroberta":
            #Se scelto distilroberta tengo solo risultati col sentimento selezionato in un dizionario
            for hit in self.raw_results:
                if hit["distilroberta_sentimento"] == self.sentiment:
                    result=dict()
                    result.update(dict(hit)) #aggiunge tutti i campi
                    print(result)
                    self.results.append(result)

            return self.order_results()

        #Se scelto vader o textblob creo dizionario coi risultati
        elif self.sentiment_tool == "Vader" or self.sentiment_tool == "TextBlob":
            for hit in self.raw_results:
                result = dict()
                result.update(dict(hit))  # aggiunge tutti i campi
                self.results.append(result)

            return self.order_results()

    def order_results(self):

        if self.sentiment_tool=="distilroberta":
            sent_ord = sorted(self.results, key=lambda d: d['distilroberta_sentimento_valore'], reverse=True)

        #???? Usiamo valore compound o i valori singoli? ?????
        elif self.sentiment_tool=="Vader":
            if self.sentiment=="positivo":
                sent_ord = sorted(self.results, key=lambda d: d['vader_valore_positivo'], reverse=True)
            elif self.sentiment=="neutrale":
                sent_ord = sorted(self.results, key=lambda d: d['vader_valore_neutrale'],reverse=True)
            else: #Sentimento negativo
                sent_ord = sorted(self.results, key=lambda d: d['vader_valore_negativo'], reverse=True)

        elif self.sentiment_tool=="TextBlob": #usato textblob
            if self.sentiment == "positivo":
                sent_ord = sorted(self.results, key=lambda d: d['textblob_valore_positivo'],reverse=True)
            else: #???? Se negativo (come faccio neutrale???) ?????
                sent_ord = sorted(self.results, key=lambda d: d['textblob_valore_positivo'])

        return sent_ord

    def check_sentiment(tool_name):
        if tool_name == "Vader" or tool_name=="Roberta":
            return True
        return False