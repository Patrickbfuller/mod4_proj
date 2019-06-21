from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd
from nltk import word_tokenize



class TextTransformer(BaseEstimator, TransformerMixin):
    
    def __init__(self):
        self.dimensions = 0
    
    def fit(self, X, y):
        return self
    
    def transform(self, X):
        """Element wise tokenize text values in a column."""
        print(type(X))
#         return np.vectorize(word_tokenize)(X)
        return np.array([word_tokenize(x) for x in X])
        return X.map(word_tokenize)
    
# tok = np.vectorize(word_tokenize)

# class ColumnTokenizer(BaseEstimator, TransformerMixin):
    
#     def __init__(self, tok=tok):
#         self.dimensions = 0
    
#     def fit(self, X, y):
#         return self
    
#     def transform(self, X):
#         """Element wise tokenize text values in a column."""
#         return tok(X)

class W2vVectorizer(BaseEstimator, TransformerMixin):
    
    def __init__(self, w2v):
        # takes in a dictionary of words and vectors as input
        self.w2v = w2v
        if len(w2v) == 0:
            self.dimensions = 0
        else:
            self.dimensions = len(w2v[next(iter(w2v))])

    def fit(self, X, y):
        return self
            
    def transform(self, X):
        """Returns the average of the vectors for each word in each row."""
        return np.array([
            np.mean([self.w2v[w] for w in words if w in self.w2v]
                   or [np.zeros(self.dimensions)], axis=0) for words in X])