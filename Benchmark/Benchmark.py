from Search_and_Result.Searcher import *
from Search_and_Result.Results import *
import math

queries = {
    "r1": "love AND stories",
    "r2": "DVD OR VHS",
    "r3": "bad AND packing",
    "r4": "worth buying",
    "r5": "background music",
    "r6": "amazing visual effects",
    "r7": "cast ",
    "r8": "faithful to the book",
    "r9": "Oscar OR awards ",
    "r10": "highest rated",
}

search = Index_Searcher(index="../Benchmark/benchmark_index")







































# with open("out.txt", 'w') as f:
#     import sys
#
#     sys.stdout = f
#     for cont, q in enumerate(queries.values()):
#         relevant_results = search.submit_query(q, results_threshold=100, ricerca_precisa=False)
#         try:
#
#             results = Results("Vader", "positive", relevant_results)
#             sent_ord_results = results.generate_results()
#         except TypeError:
#             print("niente risultati")
#             continue
#
#         print(f"{cont + 1}\t 'quarries: '\t{q}\t\t\t{len(sent_ord_results)}\t\t\t\trisultati")
#
#         #   print(cont+1," Query: ",q)
#         #   results.print_results_txt(sent_ord_results,'console')
#         for result in relevant_results:
#             print(f"\t DCG = 1 \t\t\t\t\t{result['pk']} \t {result['reviewText']} ")
