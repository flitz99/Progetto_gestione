class recensione:
    def __init__(self, *args):
        self.pk = args[0]
        self.reviewerName = args[1]
        self.reviewText = args[2]
        self.asin = args[3]
        self.title = args[4]
        self.main_cat = args[5]

        # appena creato uso il review text appena ricevuto per calcolare i score
        self.__score_myself__(self.reviewText)

    def __iter__(self):
        return iter([self.pk, self.reviewerName, self.reviewText, self.asin, self.title, self.main_cat])

    def __repr__(self):
        return f"{self.pk} | {self.reviewerName} | {self.reviewText} | {self.asin} | {self.title}  | {self.main_cat} "

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
