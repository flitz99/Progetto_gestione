class recensione:
    def __init__(self, *args):
        self.pk = args[0]
        self.reviewerName = args[1]
        self.reviewText = args[2]
        self.asin = args[3]
        self.title = args[4]
        self.main_cat = args[5]
        dict_vader = args[6]
        self.vader_valore_negativo = dict_vader['neg']
        self.vader_valore_neutrale = dict_vader['neu']
        self.vader_valore_positivo = dict_vader['pos']
        self.vader_valore_compound = dict_vader['compound']
        dict_distilroberta = args[7]
        self.distilroberta_sentimento = dict_distilroberta[0]['label']
        self.distilroberta_sentimento_valore = dict_distilroberta[0]['score']
        dict_textblob = args[8]
        self.textblob_valore_positivo = dict_textblob['polarity']
        self.textblob_valore_compound = dict_textblob['subjectivity']


        # appena creato uso il review text appena ricevuto per calcolare i score
        self.__score_myself__(self.reviewText)

    def __iter__(self):
        return iter([self.pk, self.reviewerName, self.reviewText, self.asin, self.title, self.main_cat ,
                     self.vader_valore_negativo , self.vader_valore_neutrale , self.vader_valore_positivo, self.vader_valore_compound,
                     self.distilroberta_sentimento , self.distilroberta_sentimento_valore,
                     self.textblob_valore_positivo, self.textblob_valore_compound
                     ])

    def __repr__(self):
        return f"{self.pk} | {self.reviewerName} | {self.reviewText} | {self.asin} | {self.title}  | {self.main_cat} |" \
               f"{self.vader_valore_negativo} | {self.vader_valore_neutrale}  |  {self.vader_valore_positivo}  |" \
               f"{self.vader_valore_compound} | {self.distilroberta_sentimento_valore} {self.textblob_valore_positivo}" \
               f"{self.textblob_valore_compound}"



    def __score_myself__(self, Text):
        self.vader_score = (Text)

    def get_pk(self):
        return self.pk

    def get_reviewerName(self):
        return self.reviewerName

    def get_reviewText(self):
        return self.reviewText

    def count_review(self):
        return len(self.reviewText)

    def get_asin(self):
        return self.asin

    def get_title(self):
        return self.title

    def get_main_cat(self):
        return self.main_cat
