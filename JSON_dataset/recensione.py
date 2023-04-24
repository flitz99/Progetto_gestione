''''
f.writerow(["pk", "reviewerName", "reviewText", "asin", "title", "main_cat"])


  <   >    span=
'''


b = "Great. I love Amazon."

print(len(b))

class recensione:
    def __init__(self, *args):
        self.pk = args[0]
        self.reviewerName = args[1]
        self.reviewText = args[2]
        self.asin = args[3]
        self.title = args[4]
        self.main_cat = args[5]

    def __iter__(self):
        return iter([self.pk, self.reviewerName, self.reviewText, self.asin, self.title, self.main_cat])

    def __repr__(self):
        return f"{self.pk} | {self.reviewerName} | {self.reviewText} | {self.asin} | {self.title}  | {self.main_cat} "



    def get_pk(self):
        return self.pk

    def get_reviewerName(self):
        return self.reviewerName

    def get_reviewText(self):
        return self.reviewText

    def get_asin(self):
        return self.asin

    def get_title(self):
        return self.title

    def get_main_cat(self):
        return self.main_cat