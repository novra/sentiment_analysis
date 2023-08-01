from page.fetch import*
import streamlit as st
import pandas as pd
import dask.dataframe as dd
import numpy as np
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import csv
import matplotlib.pyplot as plt

# Menginstall packege NLTK
nltk.download('vader_lexicon')

# Memuat sentimen intensity analyzer
sia = SentimentIntensityAnalyzer()

# Fungsi untuk menampilkan analisis se4ntimen dengan VADERe:\aplikasi\page\ConfusionMatrixVader.py
def perform_sentiment_analysis(text):
    scores = sia.polarity_scores(text)
    return scores['compound'], scores['neg'], scores['neu'], scores['pos']

# Fungsi untuk menyimpan sentimen score ke dalam file csv
def save_sentiment_scores(sentiment_scores, csv_file):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Compound', 'Negative', 'Neutral', 'Positive'])
        for sentiment in sentiment_scores:
            writer.writerow([sentiment[0], sentiment[1], sentiment[2], sentiment[3]])

# Fungsi untuk menampilkan diagram hasil analisis sentiment
def plot_sentiment_analysis(sentiment_scores):
    pos_count = sum(1 for sentiment in sentiment_scores if sentiment[0] > 0)
    neg_count = sum(1 for sentiment in sentiment_scores if sentiment[0] < 0)
    neu_count = sum(1 for sentiment in sentiment_scores if sentiment[0] == 0)
    labels = ['Positive', 'Negative', 'Neutral']
    counts = [pos_count, neg_count, neu_count]
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    ax.set_title('Sentiment Analysis of Tweets')
    st.pyplot(fig)

def main():
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Analisis Sentimen Menggunakan Vader</p>', unsafe_allow_html=True)
    # Upload file xlsx yang mengandung tweet clean
    tweet_file = st.file_uploader("Upload file", type="xlsx")
    if tweet_file is not None:
        # Membaca file xlsx ke dalam pandas
        tweet_df = pd.read_excel(tweet_file)

        # Menampilkan analisis sentimen setiap tweet
        sentiment_scores = []
        for tweet in tweet_df['tweet_clean']:
            scores = perform_sentiment_analysis(tweet)
            sentiment_scores.append(scores)

        # Menambahkan sentimen score ke dalam Dataframe
        tweet_df['Compound'] = [score[0] for score in sentiment_scores]
        tweet_df['Negative'] = [score[1] for score in sentiment_scores]
        tweet_df['Neutral'] = [score[2] for score in sentiment_scores]
        tweet_df['Positive'] = [score[3] for score in sentiment_scores]

        # menampilkan data frame
        st.write(tweet_df)

        # menyimpan sentiment score ke dalam file csv
        csv_file = 'Hasil vader.csv'
        save_sentiment_scores(sentiment_scores, csv_file)
        st.success("Sentiment scores saved to Hasil Vader.csv")

        # Diagram yang akan menampilkan hasil analisis
        plot_sentiment_analysis(sentiment_scores)

if __name__ == "__main__":
    main()






