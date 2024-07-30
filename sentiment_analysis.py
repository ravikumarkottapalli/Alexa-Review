#import pickle
import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
#from PIL import Image




#model = pickle.load(open(r"estimator1.pkl","rb"))
sent = SentimentIntensityAnalyzer()
text = st.text_input("Enter the text:")
if st.button("Submit"):
    if not isinstance(text, str):
        st.write("unknown")
    score =sent.polarity_scores(text)['compound']
    if score>=0.1:
        st.write("positive")
    elif score<= (-0.1):
        st.write("Negative")
    else:
        st.write("Neautral") 