import os.path
from whoosh import fields, index, qparser
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import Schema, TEXT, ID, NUMERIC
from tqdm import tqdm

class Indexer:

    def __init__(self, database, nome_dir= "indexdir_2.0"):
        self.database = database  # classe database
        self.schema = Schema(
            pk=ID(stored=True, analyzer=StemmingAnalyzer()),
            reviewerName=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            reviewText=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            asin=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            title=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            categoria=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            vader_valore_negativo=NUMERIC(float, stored=True),
            vader_valore_neutrale=NUMERIC(float, stored=True),
            vader_valore_positivo=NUMERIC(float, stored=True),
            vader_valore_compound=NUMERIC(float, stored=True),
            distilroberta_sentimento=TEXT(stored=True, analyzer=StemmingAnalyzer()),
            distilroberta_sentimento_valore=NUMERIC(float, stored=True),
            textblob_valore_polarita=NUMERIC(float, stored=True),
            textblob_valore_soggetivita=NUMERIC(float, stored=True)
        )
        self.nome_cartella = nome_dir
        if not os.path.exists(self.nome_cartella):
            os.mkdir(self.nome_cartella)

        self.ix = index.create_in(self.nome_cartella, self.schema)
        self.w = self.ix.writer()

    def create_index(self):
        for item in tqdm(self.database.lista_recensioni):
            self.w.add_document(
                pk=item[0],
                reviewerName=item[1],
                reviewText=item[2],
                asin=item[3],
                title=item[4],
                categoria=item[5],
                vader_valore_negativo=item[6],
                vader_valore_neutrale=item[7],
                vader_valore_positivo=item[8],
                vader_valore_compound=item[9],
                distilroberta_sentimento=item[10],
                distilroberta_sentimento_valore=item[11],
                textblob_valore_polarita=item[12],
                textblob_valore_soggetivita=item[13]

            )

        self.w.commit()


