''''
f.writerow(["pk", "reviewerName", "reviewText", "asin", "title", "main_cat"])


  <   >    span=
'''


class recensione:
    def __init__(self, pk, reviewer_name, review_text, asin, title, main_cat):
        self.pk = pk
        self.reviewerName = reviewer_name
        self.reviewText = review_text
        self.asin = asin
        self.title = title
        self.main_cat = main_cat

    def __iter__(self):
        return iter([self.pk, self.reviewerName, self.reviewText, self.asin, self.title, self.main_cat])

    def __repr__(self):
        return f"{self.pk} | {self.reviewerName} | {self.reviewText} | {self.asin} | {self.title}  | {self.main_cat} "

    def recensione_to_tuple(self):
        return self.pk, self.reviewerName, self.reviewText, self.asin, self.title, self.main_cat
