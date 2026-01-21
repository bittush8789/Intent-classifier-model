import os, joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

X=[ "hi","hello","how to reset password","cancel my subscription","great service" ]
y=[ "greeting","greeting","question","complaint","praise" ]

pipeline=Pipeline([("vect",CountVectorizer()),("clf",MultinomialNB())])
pipeline.fit(X,y)

os.makedirs("model/artifacts", exist_ok=True)
joblib.dump(pipeline, "model/artifacts/intent_model.pkl")
print("trained")
