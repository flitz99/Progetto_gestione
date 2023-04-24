import os.path
from datetime import datetime, timedelta
from whoosh import fields, index, qparser
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, TEXT, ID
from whoosh.index import open_dir

from Database import Database
from tqdm import tqdm


class Indexer:

    def __init__(self, database):
        self.database = database  # classe database
        self.schema = Schema(
            pk=ID(stored=True, analyzer=StemmingAnalyzer()),
            reviewerName=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            reviewText=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            asin=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            title=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            categoria=TEXT(stored=True, analyzer=StemmingAnalyzer())
        )
        self.nome_cartella = "indexdir"
        if not os.path.exists(self.nome_cartella):
            os.mkdir(self.nome_cartella)

        self.ix = index.create_in(self.nome_cartella, self.schema)
        self.w = self.ix.writer()

    def create_index(self):
        for recensione in tqdm(self.database.lista_recensioni):
            self.w.add_document(
                pk=recensione.get_pk(),
                reviewerName=recensione.get_reviewerName(),
                reviewText=recensione.get_reviewText(),
                asin=recensione.get_asin(),
                title=recensione.get_title(),
                categoria=recensione.get_main_cat()
            )

        self.w.commit()


''''
db = Database('../JSON_dataset/dataset.csv')
db.init_DB()
db.Test()

index = Indexer(db)
index.create_index()


if index.ix.is_empty() == True:
    print("fallimento")
'''

from whoosh.query import Every
ix = open_dir('./indexdir')

print(ix.schema)
#results = ix.searcher().search(Every('pk'))

#for x in results:
#    print(x)


with ix.searcher() as searcher:
    print("sono dentro")
    list(searcher.lexicon("reviewText"))


from whoosh.qparser import QueryParser

qp = QueryParser("reviewText", schema=ix.schema)
q = qp.parse(u"segment")

with ix.searcher() as s:
    results = s.search_page(q, 5, pagelen=20)
    for x,y in enumerate(results):
        print(x+1)
        print(y)

