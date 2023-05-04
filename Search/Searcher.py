import whoosh.scoring
from whoosh.index import open_dir
from whoosh.lang.wordnet import Thesaurus
from whoosh import qparser as qp
from whoosh.lang.porter import stem
import time

class Index_Searcher:

    def __init__(self, *args):

        self.ix = None
        self.thesaurus = None
        self.searcher=None
        self.parser=None
        self.inizializza()

    def inizializza(self):

        # ----  Apertura indice whoosh   ----
        try:
            self.ix = open_dir('../Indexing/indexdir')
        except:
            raise OSError("Directory non trovata")

        # print("index aperto")

        # ---- Apertura Thesaurus ----
        with open("../prolog/wn_s.pl") as file:
            self.thesaurus = Thesaurus.from_file(file)

        #Creo parser per ricerca
        orsearch = qp.OrGroup.factory(0.8) #Coefficiente che premia duplicati a discapito delle parole consecutive
        self.parser = qp.MultifieldParser("fields",self.ix.schema,group=orsearch)

        #Creo whoosh searcher
        scoring=eval("scroing.{}()".format("TF_IDF")) #passo sistema di scoring da adottare
        self.searcher= self.ix.searcher(weighting=scoring)

    def submit_query(self,query,results_threshold=100,expand=False):

        #Creare sinonimi delle forme basi dei vocaboli nella query
        words = [stem(i) for i in query.split()] #stemming sulla query

        sinonimi= [j for i in words for j in self.thesaurus.synonyms(i)] #Acquisisco sinonimi della query
        words.extend(sinonimi) #estendo la parola aggiungendo sinonimi

        query_expanded=" ".join(words)
        query= self.parser.parse(query_expanded)

        #tempo esecuzione ....






















# from whoosh.qparser import QueryParser
#
# qparser = QueryParser("reviewText", schema=ix.schema)
# q = qparser.parse(u"segment")
#
# with ix.searcher() as s:
#     results = s.search_page(q, 5, pagelen=20)
#     for x, y in enumerate(results):
#         print(x + 1)
#         print(y)
#
# # ---- Apertura thesaurus wordnet da file ---
# with open("./wn_s.pl") as f:
#     thesaurus = Thesaurus.from_file(f)
#
# # ---- Parser  ----
# orgroup = qp.OrGroup.factory(0.8)
#
#
