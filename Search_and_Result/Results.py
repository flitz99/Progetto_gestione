import sys


class Results:
    '''
         Ingresso risultati, analizzatore , sentimento_passato
         - riordinare
         - filtraggio selettivo
         - ranking function -> ordina i risultati in base alla combinazione
                                punteggio di pertinenza + punteggio di sentiment
        uscita lista oridnata
    '''

    def __init__(self, tool_name, sentiment, results, ranking_fun="balanced_weighted_avg"):

        self.sentiment_tool = tool_name
        self.sentiment = sentiment
        self.raw_results = results
        self.results = None

    def generate_results_benchmark(self):
        '''
        si occupa di gestire i risultati trovati dalle querries
        :return: la lista dei risultati
        '''
        self.results = []    #

        if self.sentiment_tool == "Vader": #sempre Vader
            for cont, hit in enumerate(self.raw_results):
                result = dict()
                result.update(dict(hit))  # aggiunge tutti i campi
                result["pos_pertinenza"] = cont + 1
                self.results.append(result)

        return self.order_results()

    def generate_results(self):
        '''
        prende i risultati trovati nell'index e li trasforma in un dizionario
        :return:  la funzione di ordinamento, chiamata con il dizionario appena creato
        '''

        self.results = []

        if self.sentiment_tool == "distilroberta":
            # Se scelto distilroberta tengo solo risultati col sentimento selezionato in un dizionario
            for cont, hit in enumerate(self.raw_results):
                if hit["distilroberta_sentimento"] == self.sentiment:
                    result = dict()
                    result["pk"] = hit["pk"]
                    result["title"] = hit["title"]
                    result["categoria"] = hit["categoria"]
                    result["reviewerName"] = hit["reviewerName"]
                    result["reviewText"] = hit["reviewText"]
                    result["distilroberta_sentimento_valore"] = hit["distilroberta_sentimento_valore"]
                    result["textblob_valore_polarita"] = hit["textblob_valore_polarita"]
                    result["pos_pertinenza"] = cont + 1
                    # result.update(dict(hit)) #aggiunge tutti i campi
                    self.results.append(result)

            return self.order_results()

        # Se scelto vader
        elif self.sentiment_tool == "Vader":
            for cont, hit in enumerate(self.raw_results):
                result = dict()
                result["pk"] = hit["pk"]
                result["title"] = hit["title"]
                result["categoria"] = hit["categoria"]
                result["reviewerName"] = hit["reviewerName"]
                result["reviewText"] = hit["reviewText"]
                result["vader_valore_positivo"] = hit["vader_valore_positivo"]
                result["vader_valore_neutrale"] = hit["vader_valore_neutrale"]
                result["vader_valore_negativo"] = hit["vader_valore_negativo"]
                result["pos_pertinenza"] = cont + 1
                self.results.append(result)

            return self.order_results()

        # Se scelto Textblob
        elif self.sentiment_tool == "TextBlob":
            for cont, hit in enumerate(self.raw_results):
                result = dict()
                result["pk"] = hit["pk"]
                result["title"] = hit["title"]
                result["categoria"] = hit["categoria"]
                result["reviewerName"] = hit["reviewerName"]
                result["reviewText"] = hit["reviewText"]
                result["textblob_valore_polarita"] = hit["textblob_valore_polarita"]
                result["pos_pertinenza"] = cont + 1
                self.results.append(result)

            return self.order_results()

    def order_results(self):
        '''
            Ordina i risultati per valore di sentimetno pre-calcolato
            positivo in modo decrescente
            negativo in modo cerscente
        :return:
        '''

        if self.sentiment_tool == "distilroberta":
            sent_ord = sorted(self.results, key=lambda d: d['distilroberta_sentimento_valore'], reverse=True)

        elif self.sentiment_tool == "Vader":
            if self.sentiment == "positivo":
                sent_ord = sorted(self.results, key=lambda d: d['vader_valore_positivo'], reverse=True)
            elif self.sentiment == "neutrale":
                sent_ord = sorted(self.results, key=lambda d: d['vader_valore_neutrale'], reverse=True)
            else:  # Sentimento negativo
                sent_ord = sorted(self.results, key=lambda d: d['vader_valore_negativo'], reverse=True)

        elif self.sentiment_tool == "TextBlob":
            if self.sentiment == "positivo":
                sent_ord = sorted(self.results, key=lambda d: d['textblob_valore_polarita'], reverse=True)
            else:
                sent_ord = sorted(self.results, key=lambda d: d['textblob_valore_polarita'])

        for cont, hit in enumerate(sent_ord):
            hit["pos_sentiment"] = cont + 1

        for hit in sent_ord:
            hit["ranking"] = hit["pos_sentiment"] * hit["pos_pertinenza"]

        sent_ord = sorted(sent_ord, key=lambda d: d['ranking'])

        return sent_ord

    def print_results_txt(self, results, output='console', nome_file='output.txt', limit=100):
        '''

        Funzione che si occupa del printing dei risultati

        :param results: lista di risultati da stampare
        :param output:  di base "console" se terminale o possiamo specificare il nome del file 'txt' dove salvarlo
        :return:
        '''

        if not output == 'console':
            import sys
            f = open(nome_file, 'w')
            sys.stdout = f

        print('---------------------------------------------------- RISULTATI ----------------------------------------------------')
        for cont, r in enumerate(results):
            if cont == limit:
                break
            print("Ranking_finale: ", cont+1)
            print(f"Categoria: {r['categoria']}, Nome del prodotto : {r['title']} ")
            print(f"Autore recensione: {r['reviewerName']}")
            print(f"Testo recensione: {r['reviewText']}")
            print(f"Ranking pertinenza: {r['pos_pertinenza']}  ")
            print(f"Ranking sentimento: {r['pos_sentiment']}  ")
            print(f"Sentiment analyzer: {self.sentiment_tool} ")
            if self.sentiment_tool == 'Vader':
                if self.sentiment == 'positivo':
                    print(f"valore_sentimento = {r['vader_valore_positivo']}")
                if self.sentiment == 'neutrale':
                    print(f"valore_sentimento = {r['vader_valore_neutrale']}")
                if self.sentiment == 'negativo':
                    print(f"valore_sentimento = {r['vader_valore_negativo']}")
            if self.sentiment_tool == "TextBlob":
                print(f"valore_sentimento = {r['textblob_valore_polarita']}")
            if self.sentiment_tool == 'distilroberta':
                print(f"valore_sentimento = {r['distilroberta_sentimento_valore']} ")
                print(f"valore_sentimento = {r['textblob_valore_polarita']}")

            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

        if not output == 'console':
            f.close()
