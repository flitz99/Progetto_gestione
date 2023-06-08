from Indexing_Database import Indexing as indx
from Indexing_Database import Database as datab
import csv
from whoosh.fields import Schema, TEXT, ID, NUMERIC
from whoosh.analysis import StemmingAnalyzer
from whoosh import index
from tqdm import tqdm


def create_benchmark():
    '''
    usando il file CSV della sentiment prendiamo casualmente 100 entries per creare un csv con campi vuoti
    per inserire il voto del DCG a mano
    :return:
    '''
    db = datab.Database('../JSON_dataset/dataset_sentiment.csv')
    db.init_DB()
    db.Benchmark_mode()  # sceglie 100 recensioni di film a caso
    a = len(db.lista_recensioni)
    print(a)


    if a == 100:
        index = indx.Indexer(db, 'index_benchmark')
        index.create_index()

        if index.ix.is_empty() == True:
            print("fallimento")
        else:

            temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for rec in db.lista_recensioni:
                rec.extend(temp)

            with open('benchmark.csv', 'w') as f:

                # using csv.writer method from CSV package
                write = csv.writer(f)
                fields = ['pk', 'reviewerName', 'reviewText', 'asin', 'title', 'main_cat',
                          'vader_valore_negativo', 'vader_valore_neutrale', 'vader_valore_positivo',
                          'vader_valore_compound', 'distilroberta_sentimento', 'distilroberta_sentimento_valore',
                          'textblob_valore_polarita', 'textblob_valore_soggettivita',
                          'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10']
                write.writerow(fields)
                write.writerows(db.lista_recensioni)

    else:
        print("fallimento")


def create_index_from_csv():
    '''
    Crea un index whoosh a partire da un file CSV
    :return: nullo

    '''
    print("index non esiste attendere la sua creazione")
    db = datab.Database('../Progetto_gestione/Benchmark_folder/benchmark_DCG.csv')
    db.init_DB()

    # for l in db.lista_recensioni:
    #     print(l)

    schema_benchmark = Schema(
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
        textblob_valore_soggetivita=NUMERIC(float, stored=True),
        r1=NUMERIC(float, stored=True),
        r2=NUMERIC(float, stored=True),
        r3=NUMERIC(float, stored=True),
        r4=NUMERIC(float, stored=True),
        r5=NUMERIC(float, stored=True),
        r6=NUMERIC(float, stored=True),
        r7=NUMERIC(float, stored=True),
        r8=NUMERIC(float, stored=True),
        r9=NUMERIC(float, stored=True),
        r10=NUMERIC(float, stored=True)
    )
    nome_cartella = 'benchmark_index'
    import os
    if not os.path.exists(nome_cartella):
        os.mkdir(nome_cartella)
    index_creator = index.create_in(nome_cartella, schema_benchmark)
    index_writer = index_creator.writer()

    for item in tqdm(db.lista_recensioni):
        index_writer.add_document(
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
            textblob_valore_soggetivita=item[13],
            r1=item[14],
            r2=item[15],
            r3=item[16],
            r4=item[17],
            r5=item[18],
            r6=item[19],
            r7=item[20],
            r8=item[21],
            r9=item[22],
            r10=item[23]

        )

    index_writer.commit()

'''
non neccesario crearlo siccome `e stato già creato a mano e assegnato manualmente un ranking per 
calcolare il DCG
'''
# create_index_from_csv()