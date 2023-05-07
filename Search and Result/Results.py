
class Results:
        def __init__(self,tool_name,sentiment,results, textual_field = "text",ranking_fun = "balanced_weighted_avg"):

            self.sentiment_tool=tool_name
            self.results = self.generate_results(results,"field")
            self.ordered_results=None

        def generate_results(self, results,textual_field):

        
                if not results:
                    raise Exception("Nessun risultato per questa query")

                self.ordered_results=[]

                for hit in results:
                    result=dict()
                    result["docnum"]=hit.docnum
                    result.update(dict(hit))
                    result["pert_score"]=hit.score
                    result["sent_score"]=hit.sentiment_score

                    self.ordered_results.append(result)

                return "prova"

        def check_sentiment(tool_name):
            if tool_name == "Vader" or tool_name=="Roberta":
                return True
            return False