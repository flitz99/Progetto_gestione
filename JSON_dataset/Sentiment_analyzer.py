from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline
from textblob import TextBlob

#
#  vader            https://github.com/cjhutto/vaderSentiment
#  distilroberta    https://github.com/j-hartmann/emotion-english-distilroberta-base
#  TextBlob        https://github.com/sloria/TextBlob

class Sentiment_analyzers:

    def __init__(self):
        # inizializzo vader
        self.vader = SentimentIntensityAnalyzer()

        # inizializzo distilroberta
        self.distilroberta = pipeline("sentiment-analysis",
                                      model="j-hartmann/emotion-english-distilroberta-base")

    def Analizza_Vader(self, testo_da_analizzare):
        return self.vader.polarity_scores(testo_da_analizzare)

    def Analizza_Distilroberta(self, testo_da_analizzare):
        return self.distilroberta(testo_da_analizzare)

    def Anilizza_Textblob(self,testo_da_analizzare):
        testimonial = TextBlob(testo_da_analizzare)
        testimonial_dict = {}
        testimonial_dict.update({"polarity":testimonial.sentiment.polarity})
        testimonial_dict.update({"subjectivity": testimonial.sentiment.subjectivity})
        return testimonial_dict
