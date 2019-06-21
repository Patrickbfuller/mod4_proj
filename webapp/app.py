import random
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn_pandas import DataFrameMapper
from sklearn_pandas.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor



from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize

from flask import Flask, request, render_template, jsonify


from . import vectorizer



with open('log_score_model.pkl', 'rb') as f:
    score_model = pickle.load(f)
    
with open('log_comment_model.pkl', 'rb') as f:
    comment_model = pickle.load(f)

app = Flask(__name__, static_url_path="")

def day_str_to_int(text):
    if text == 'Monday':
        return 0
    if text == 'Tuesday':
        return 1
    if text == 'Wednesday':
        return 2
    if text =='Thursday':
        return 3
    if text == 'Friday':
        return 4
    if text =='Saturday':
        return 5
    if text == 'Sunday':
        return 6

@app.route('/')
def index():
    """Return the main page."""
    return render_template('theme.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Return a random prediction."""
    data = request.json
    print(data)
    
    hour_24_text = data['user_input_hour']
    print(hour_24_text, type(hour_24_text))
    hour_24 = int(hour_24_text)
    
    weekday_str = data['user_input_weekday']
    weekday_int = day_str_to_int(weekday_str)
    
    age_hours_text = data['user_input_age']
    age_hours = int(age_hours_text)
    age_mins = age_hours * 60
    
    text = data['user_input_text']
    
    arguments = (hour_24, weekday_int,
                age_mins, text)
    arguments = pd.DataFrame(
        [[text, age_mins, weekday_int, hour_24]],
        columns=['text', 'age', 'weekday_posted', 'hour_posted'])


    
    # prediction = model.predict_proba([data['user_input']])
    
    predicted_score = np.exp(score_model.predict(arguments))
    predicted_comments = np.exp(comment_model.predict(arguments))
    
    
    return jsonify({'1. Score': predicted_score[0],
                    '2. Number of Comments': predicted_comments[0]})








# # Miles-ish template below

# with open('spam_model.pkl', 'rb') as f:
#     model = pickle.load(f)
# app = Flask(__name__, static_url_path="")

# @app.route('/')
# def index():
#     """Return the main page."""
#     return render_template('theme.html')


# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     """Return a random prediction."""
#     data = request.json
#     prediction = model.predict_proba([data['user_input']])
#     return jsonify({'1. Score': prediction[0][1], '2. Number of Comments': 0})

