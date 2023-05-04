from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline


#
#  vader            https://github.com/cjhutto/vaderSentiment
#  distilroberta    https://github.com/j-hartmann/emotion-english-distilroberta-base

class Sentiment_analyzers:

    def __init__(self):
        # inizializzo vader
        self.vader = SentimentIntensityAnalyzer()

        # inizializzo distilroberta
        self.distilroberta = pipeline("sentiment-analysis", model="j-hartmann/emotion-english-distilroberta-base")

    def Analizza_Vader(self, testo_da_analizzare):
        return self.vader.polarity_scores(testo_da_analizzare)

    def Analizza_Distilroberta(self, testo_da_analizzare):
        return self.distilroberta(testo_da_analizzare)


text = "One of my very favourite albums from one of my very favourite singers.  I was happy to see I could replace the old worn cassettes from years ago."
classe = Sentiment_analyzers()  # creo la classe
print("darth Vader")
print(classe.Analizza_Vader(text))  # calcola
print("distilroberta")
print(classe.Analizza_Distilroberta(text))