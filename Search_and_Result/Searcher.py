from whoosh import scoring
from whoosh.index import open_dir
from whoosh.lang.wordnet import Thesaurus
from whoosh import qparser as qp
from whoosh.lang.porter import stem

from whoosh.qparser import QueryParser


class Index_Searcher:

    def __init__(self, algoritmo_di_ricerca = None):

        # ----  Apertura indice whoosh   ----
        try:
            self.ix = open_dir('../Search_and_Result/indexdir_2.0')
        except:
            raise OSError("Directory non trovata")

        # ---- Apertura Thesaurus ----
        with open("../prolog/wn_s.pl") as file:
            self.thesaurus = Thesaurus.from_file(file)

        if algoritmo_di_ricerca == "BM25F":
            print("hai scelto di usare BM25F")
            self.src = self.ix.searcher(weighting=scoring.BM25F)
        else:
            print("hai scelto di usare TF_IDF")
            self.src = self.ix.searcher(weighting=scoring.TF_IDF())

    def submit_query(self, query, results_threshold=100, ricerca_precisa=False):

        if query[0] == '"' and query[-1] == '"':
            # significa che utente vuole la ricerca precisa quindi
            ricerca_precisa = True

        # se non è una ricerca precisa, cerca anche i sinonimi delle parole immesse
        if not ricerca_precisa:
            words = [stem(i) for i in query.split()]  # separo le parole
            sinonimi = [j for i in words for j in self.thesaurus.synonyms(i)]  # cerco sinonimi singole parole
            words.extend(sinonimi)  # aggiungo alla lista di ricerca
            stinga_di_ricerca = " ".join(words)  # trasforma la lista in una stringa_di_ricerca

            self.parser = qp.MultifieldParser(["reviewText"], schema=self.ix.schema, group=qp.OrGroup).parse(
                 stinga_di_ricerca)

            query_di_ricerca = self.src.search(self.parser, limit=results_threshold)

        else:
            self.parser = qp.MultifieldParser(["reviewText"], schema=self.ix.schema, group=qp.OrGroup).parse(
                query)

            query_di_ricerca = self.src.search(self.parser, limit=results_threshold)

        if query_di_ricerca:
            print("Sono presenti risultati")
            return query_di_ricerca
        else:
            print("Errore nella query")

    def Test_Controllo_Index(self, testo_test):
        ix = open_dir('../Indexing_Database/indexdir_2.0')

        qparser = QueryParser("reviewText", schema=ix.schema)
        q = qparser.parse(testo_test)

        with ix.searcher() as s:
            results = s.search_page(q, 5, pagelen=20)
            for x, y in enumerate(results):
                print(x + 1)
                print(y)
