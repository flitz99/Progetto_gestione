from Search_and_Result.Searcher import *
from Search_and_Result.Results import *
import math

queries = {
    "r1": "sing OR dance",
    "r2": "young AND kids",
    "r3": "bad packing",
    "r4": "worth buying",
    "r5": "background music",
    "r6": "amazing animation",
    "r7": "shipping time",
    "r8": "faithful to the book",
    "r9": "strong  female lead",
    "r10": "band OR group",
}

search = Index_Searcher(index="../Benchmark/index_benchmark")

for cont, q in enumerate(queries.values()):
    relevant_results = search.submit_query(q, results_threshold=100, ricerca_precisa=False)
    try:

        results = Results("Vader", "positive", relevant_results)
        sent_ord_results = results.generate_results()
    except TypeError:
        print("niente risultati")
        continue

    print(f"{cont + 1}\t 'quarries: '\t{q}\t\t\t{len(sent_ord_results)}\t\t\t\trisultati")

#   print(cont+1," Query: ",q)
#   results.print_results_txt(sent_ord_results,'console')
