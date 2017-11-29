#http://docs.cs50.net/problems/sentiments/sentiments.html#walkthrough 'to deploy webserver'

from flask import Flask, redirect, render_template, request, url_for

import helpers
from analyzer import Analyzer

#imported by me
import os
import sys
import nltk
from nltk.tokenize import TweetTokenizer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    #get user screenname
    screen_name = request.args.get("screen_name", "")
    #redirect to the index if its missing
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)
    #redirect to index if None example= @kaufecake
    if not tweets:
        return redirect(url_for("index"))

    # absolute paths to lists and assign positives and negatives
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    #TODO initialize Analizer as you leran in Analyzer.py and analyze tweets
    analyzer = Analyzer(positives, negatives)

    #To analizer tweets we want to iterate over the tweets scoring all the words and calculate fi they are + - or N

    #create variables score (to save each analyze number) and nexttweet(to move to the next tweet in the loop)
    score = 0
    nexttweet = 0

    positive, negative, neutral = 0, 0, 0

    #implement tokenizertweet to separate a long string into samller (words)
    for eachtweet in tweets:
        tokenizer = TweetTokenizer()
        tkns = tokenizer.tokenize(eachtweet)
        final_score = 0
        #do something for each word:
        for tokens in tkns:
            #analyze each word and save the respective number
            score = analyzer.analyze(tokens)
            final_score = score + final_score
        if final_score >= 1:
            positive = positive + 1
        if final_score <= -1:
            negative = negative + 1
        if final_score == 0:
            neutral = neutral + 1

        #test:
        #if final_score > 0.0:
        #    print(final_score, tweets[nexttweet])
        #elif final_score < 0.0:
        #    print(final_score, tweets[nexttweet])
        #else:
        #    print(final_score, tweets[nexttweet])
        nexttweet += 1

    #print("total:",nexttweet)

    #positive, negative, neutral = 0.0, 0.0, 100.0

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
