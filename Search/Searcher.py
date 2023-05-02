from whoosh.index import open_dir
from whoosh.lang.wordnet import Thesaurus
from whoosh import qparser as qp
from whoosh.fields import *


class Searcher:

    def __init__(self, *args):

        print("inizio searcher")

    def inizializza(self):
        # ----  Apertura indice whoosh   ----
        from whoosh.query import Every
        try:
            ix = open_dir('./indexdir')
        except:
            raise OSError(" Directory non trovata")




from whoosh.qparser import QueryParser

qparser = QueryParser("reviewText", schema=ix.schema)
q = qparser.parse(u"segment")

with ix.searcher() as s:
    results = s.search_page(q, 5, pagelen=20)
    for x, y in enumerate(results):
        print(x + 1)
        print(y)

# ---- Apertura thesaurus wordnet da file ---
with open("./wn_s.pl") as f:
    thesaurus = Thesaurus.from_file(f)

# ---- Parser  ----
orgroup = qp.OrGroup.factory(0.8)
