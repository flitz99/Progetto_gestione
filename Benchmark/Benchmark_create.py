
from Indexing_Database import Indexing as indx
from Indexing_Database import Database as datab
import csv

def create_benchmark():
    db = datab.Database('../JSON_dataset/dataset_sentiment.csv')
    db.init_DB()
    db.Benchmark_mode()  # sceglie 100 recensioni a caso
    a= len(db.lista_recensioni)
    print(a)

    for b in db.lista_recensioni:
        print(b)


    if  a == 100 :
        index = indx.Indexer(db,'index_benchmark')
        index.create_index()

        if index.ix.is_empty() == True:
            print("fallimento")
        else:

            temp = [0,0,0,0,0,0,0,0,0,0]
            for rec in db.lista_recensioni :
                rec.extend(temp)


            with open('benchmark.csv', 'w') as f:

                # using csv.writer method from CSV package
                write = csv.writer(f)
                fields=['pk','reviewerName','reviewText','asin','title','main_cat',
                        'vader_valore_negativo','vader_valore_neutrale','vader_valore_positivo',
                        'vader_valore_compound','distilroberta_sentimento','distilroberta_sentimento_valore',
                        'textblob_valore_polarita','textblob_valore_soggettivita',
                        'r1','r2','r3','r4','r5','r6','r7','r8','r9','r10']
                write.writerow(fields)
                write.writerows(db.lista_recensioni)

    else:
        print("fallimento")


