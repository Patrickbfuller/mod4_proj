from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


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