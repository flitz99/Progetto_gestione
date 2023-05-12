import matplotlib.pyplot as plt
import numpy as np

queries = {
    "r1": "love AND stories",
    "r2": "DVD OR VHS",
    "r3": "bad AND packing",
    "r4": "worth buying",
    "r5": "background music",
    "r6": "amazing visual effects",
    "r7": "cast",
    "r8": "faithful to the book",
    "r9": "Oscar OR awards ",
    "r10": "highest rated",
}

import math
def calcola_dcg(lista_ordinata,dict_key):


    lista_valori_dcg = []
    for valori in lista_ordinata:
        lista_valori_dcg.append(int(valori[dict_key]))


    dcg = lista_valori_dcg[0]
    for iteratore in range(1, len(lista_valori_dcg)):
        dcg += lista_valori_dcg[iteratore] / math.log2(iteratore+1)
    return dcg



from Search_and_Result.Searcher import Index_Searcher
from Search_and_Result.Results import Results


Index_benchmark = Index_Searcher(index="../Benchmark/benchmark_index")

lunghezza_querries = []
dcg_values=[]
contatore = 0
for dict_key , dict_values in queries.items():
    relevant_results = Index_benchmark.submit_query(dict_values, results_threshold=100,
                                           ricerca_precisa=False)  # Ricerca query nell'index
    try:
            results = Results("Vader", "positive", relevant_results)
    except TypeError:
            print("niente risultati per" , dict_values)
            continue
    lunghezza_querries.append(len(relevant_results))
    order_results = results.generate_results_benchmark() #acquisisce risultati ordinati
    valore_dcg = calcola_dcg(order_results, dict_key)  # Calcolo cdg per risultati query

    ordinamento_ottimale = sorted(order_results, key=lambda d:d[dict_key] , reverse=True)
    valore_dcg_ottimale = calcola_dcg(ordinamento_ottimale, dict_key)


    temp = {}
    temp["queries"] = dict_values
    temp["DCG"] = valore_dcg
    temp["DCG_ottimale"] = valore_dcg_ottimale
    temp["NDCG"] = valore_dcg/valore_dcg_ottimale
    dcg_values.append(temp)

    #   dcg_ranking = pertinenza + sentimento       --> order_results
    #   dcg_ottimale  = in ordine del valore DCG    --> ordinamento_ottimale
    #  NDCG =  dcg_ranking / dcg_ottimale

    # print("quarries :",dict_values ,"valore dcg : ", calcola_dcg(order_results, dict_key))
    # for result in order_results:
    #     print(f"\t\t\t\t\t{result['pk']} \t  \t  {result[dict_key]}")
    # print("\n\n")

# for dict in dcg_values:
#     print(dict)
#     print()

#creazione dei grafici
def plot_graph(data, measure, file_name):
    # Asse x con le query
    queries = ["q{}".format(i) for i in range(1, len(data) + 1)]
    x = np.arange(len(queries))

    # Asse y con valori DCG o NDCG
    values = [round(dict[measure], 1) for dict in data]

    # Crea il grafico a barre
    width = 0.40
    fig, ax = plt.subplots()
    barra_valori = ax.bar(x - width / 2, values, width, label=measure , color = 'C0')
    barra_valori_recensioni = ax.bar(x + width / 2, lunghezza_querries , width, label='Retrieved recension',  color = 'C5')
    ax.bar_label(barra_valori,padding=5)
    ax.bar_label(barra_valori_recensioni,padding=5)  # offset numero per colonna

    # inserisco leggenda e labels
    ax.set_ylabel('Values')
    ax.set_title(measure + " TF-IDF+ Vader Positivo")
    ax.set_xticks(x,queries)
    ax.legend()

    # salva il grafico e lo mostra
    fig.tight_layout()
    plt.savefig(file_name)
    plt.show()

plot_graph(dcg_values,"DCG","DCG_measures.png")
plot_graph(dcg_values,"NDCG","NDCG_measures.png")
