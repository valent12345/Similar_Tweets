from flask import Flask, request, jsonify, url_for, render_template
from prometheus_client import start_http_server, Counter, Gauge, Summary
from nltk import word_tokenize, download
from nltk.corpus import stopwords
from gensim import models
from gensim.similarities import WmdSimilarity
import pandas as pd
import re
import time
import random
download('stopwords')
download('punkt')

app = Flask(__name__)

# Prometheus Monitoring
REQUESTS = Counter('page_access', 'Acces for main page')
REQUESTS_RES = Counter('res_page', 'Results for page acces')
IN_PROGRESS = Gauge('page_access_in_progress', 'Visits in progress')
LAST = Gauge('page_accesses_last_time_seconds',
             'The last time a res_page was served')
LATENCY = Summary('latency_in_secondss', 'Time for a request a result page')

stop_words = stopwords.words('english')
model = models.Word2Vec.load('word2vec.model')

df = pd.read_csv('tweets.csv')
df_text = pd.DataFrame()
df_text['Text'] = df.text
similarity_index = WmdSimilarity(df_text['Text'], model, num_best=20)


def pre_processing_text(text):
    # lowercase
    text = text.lower()
    # extra lines
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r"\'", "", text)
    # punctuations and symbols
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    # hastags
    text = text.replace("#", "")
    # hyperlinks
    text = re.sub(
        "(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)", '', text)
    text = re.sub("http", '', text)
    # retweets
    text = re.sub(r'^RT @.+\:', '', text)
    text = re.sub('@', '', text)
    # stopwords
    return [word for word in word_tokenize(text) if word not in stop_words]

@app.route('/')
def index():
    REQUESTS.inc()
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        REQUESTS.inc()
        IN_PROGRESS.inc()
        REQUESTS_RES.inc()
        start = time.time()
        answer = request.form['Answer']
        clean_answer = pre_processing_text(answer)
        similar = similarity_index[clean_answer]
        text_results = list()
        score_results = list()
        for i in range(len(similar)):
            text_results.append(df_text['Text'][similar[i][0]])
            score_results.append(similar[i][1])
        score_results = ["{:.2f}".format(score) for score in score_results]
        LAST.set(time.time())
        IN_PROGRESS.dec()
        LATENCY.observe(time.time() - start)
        return render_template('results.html', results=zip(text_results,score_results))
    return render_template('index.html')


if __name__ == "__main__":
    start_http_server(8010)
    app.run(host='0.0.0.0')
