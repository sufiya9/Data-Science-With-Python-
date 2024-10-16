import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import re # regular expression
from textblob import TextBlob


st.set_page_config(
    layout='wide'
)

st.title (''' Sentiment Analysis Using NLP 🌺😊
For Amazon reviews 💼🛍️''' )


def remove_links(feedback):
    feedback = re.sub(r'http\S+',' ',feedback ) 
    feedback = re.sub(r'www.\S+',' ',feedback ) 
    return re.sub(r'[^a-z0-9]',' ', feedback)

def get_sentiment(feedback):
    blob = TextBlob(feedback)
    return blob.sentiment.polarity

def get_sentiment_name(sentiment):
    if sentiment == 0:
        return "👎Nothing to say"
    elif sentiment > 0:
        return "👍Like most 😊"
    else:
        return "🤢 Worst❎"
    

@st.cache
def load_data():
    df=pd.read_csv('test.csv')
    df.sort_values(by='Grade',inplace=True)
    df['Sentiment'] = df['Feedback'].apply(get_sentiment)
    df['SentimentName'] = df['Sentiment'].apply(get_sentiment_name)
    return df


df = load_data()
if st.sidebar.checkbox("Show raw data"):
    st.write(df)

if st.sidebar.checkbox("Visualize"):
    st.header("Feedback sentiment Count ✅")
    counter = df.SentimentName.value_counts().reset_index()
    c1, c2 = st.columns([1,2])
    c1.write(counter)
    fig = px.bar(counter,'index','SentimentName')
    c2.plotly_chart(fig, use_container_width=True)