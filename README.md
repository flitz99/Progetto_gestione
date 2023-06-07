# Progetto_gestione

Questo è un progetto sviluppato per l'esame di gestione dell'informazione realizzato da Filippo Reggiani e Janath Uthayakumar

This is a project made for the course of Gestione di informazione of university of Computer science of  Modena made by Filippo Reggiani e Janath Uthayakumar  


## Libraries
* beautifulsoup4 `4.12.2`
* scrapy` 2.9.0`
* whoosh `2.7.4`
* tqdm `4.65.0`
* transformers `4.29.1`
* textblob `0.17.1`
* vadersentiment `3.3.2`
* tensorflow `2.12.0`
* matplotlib  `3.7.1`



## Setup 

- Pull this project in a folder using the git link

- Use a virtual environment as you like ( we tested this project with PIPENV)

- Install dependencies from the `Pipfile`

- run `Search_and_Result/Start.py` ( it will take 10 minutes )

- when everything its ready it will ask you to insert a queries ,
don't need to initialize but just run `Search_and_Result/Start.py` to make queries \


## How to querries ?

after following the steps described in the **Setup** section 

1. Run Start.py
2. insert the query to search : for example _`amazing visual effects`_
3. the application will prompt you to choose the search engine between `BM25F` or `TF_IDF` (_default is TF_IDF_)
4. the application will prompt you to choose the sentiment analyzer between `Distil-roberta `, `Textblob` and `Vader`
5. based on the analyzer chosen, you need to specify the sentiment type for example `positive` or `negative` or `neutral`
6. the result will be displayed


## output example 
the following output is an example by searching   
* amazing visual effects 
* TD_IDF
* Vader
* Negative

>`Ranking_finale`:  1 <br />
>`Categoria`: Cd e Vynil, Nome del prodotto : Pink Floyd - Pulse VHS <br />
>`Autore recensione`: Erico Macedo<br />
>`Testo recensione`: After waiting years to see Pulse on DVD, I have to say I am disappointed with the DVD. The concert is amazing, but as already posted in other reviews, it was shot in video instead of film. The result is clearly visible and the image quality is poor - too bad, as the visual effects would look amazing on a large screen.  Anyway, it is still a must-have for Pink Floyd fans. You might be a little disappointed with the image quality, but you will definitely not regret your purchase.<br />
>`Ranking pertinenza`: 2  <br />
>`Ranking sentimento`: 9  <br />
>`Sentiment analyzer`: Vader <br />

**_Ranking_finale_** =  final score obtained by combining _Ranking pertinenza_ and _Ranking sentimento_ scroes <br >
**_Categoria_** =  the category name of the product  <br >
**_Autore recensione_** =  the name of the author of the review <br >
**_Testo recensione_** =   the body of the review  <br >
**_Ranking pertinenza_** =  the ranking of the review based on the pertinence of the querries and the content of the _review_  <br >
**_Ranking sentimento_** =  the ranking based on the sentiment analyzer and sentiment chosen  <br >
**_Sentiment analyzer_** =  the sentiment analyzer used for the analyzes  <br >

## Benchmark

for the benchmark we have chosen 100 reviews randomly using `Benchmark/Benchmark_create.py` and choose 10 queries to mimic what an user would have asked

the 10 query are inside the `Benchmark/Benchmark.py`

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

t