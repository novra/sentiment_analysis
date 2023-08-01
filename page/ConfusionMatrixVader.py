import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score

def main():
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Evaluasi Matrix Vader</p>', unsafe_allow_html=True)

    # User diminta untuk memasukkan dua file, yaitu dt_tweet dan d_tweet dalam format csv
    dt_tweet_file = st.file_uploader("Upload dt_tweet file (CSV)", type="csv")
    df_tweet_file = st.file_uploader("Upload df_tweet file (CSV)", type="csv")

    if dt_tweet_file is not None and df_tweet_file is not None:
        # Membaca file dt_tweet dan df_tweet
        dt_tweet = pd.read_csv(dt_tweet_file)
        df_tweet = pd.read_csv(df_tweet_file)

        # Menampilkan dt_tweet
        st.write("dt_tweet:")
        st.write(dt_tweet)

        # Mengubah label dt_tweet
        label_dict = {'neutral': 0, 'positive': 1, 'negative': -1}
        dt_tweet['label'] = dt_tweet['label'].map(label_dict)

        # Menampilkan dt_tweet setelah pengubahan label
        st.write("dt_tweet setelah pengubahan label:")
        st.write(dt_tweet)

        # Menampilkan df_tweet
        st.write("df_tweet:")
        st.write(df_tweet)

        # Menambahkan kolom baru pada df_tweet dengan nama Sentiment_Type
        df_tweet['Sentiment_Type'] = df_tweet['Compound'].apply(lambda x: 'Positive' if x >= 0.05 else 'Negative' if x <= -0.05 else 'Neutral')

        # Mengubah label df_tweet
        label_dict = {'Neutral': 0, 'Positive': 1, 'Negative': -1}
        df_tweet['Sentiment_Type'] = df_tweet['Sentiment_Type'].apply(lambda x: label_dict[x])



        # Menampilkan df_tweet setelah penambahan kolom
        st.write("df_tweet setelah penambahan kolom Sentiment_Type:")
        st.write(df_tweet)

        # Menghitung jumlah label dengan masing-masing sentimennya pada dt_tweet
        label_counts_dt = dt_tweet['label'].value_counts()

        # Menampilkan pie chart berdasarkan dt_tweet
        plt.figure(figsize=(8, 6))
        label_counts_dt.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Persentase Sentimen dt_tweet')
        plt.axis('equal')
        st.pyplot(plt)

        # Menghitung jumlah label dengan masing-masing sentimennya
        label_counts = dt_tweet['label'].value_counts()

        # Menampilkan jumlah label dengan masing-masing sentimennya
        st.write("Jumlah label dt_tweet dengan masing-masing sentimennya:")
        st.write(label_counts)

        # Menghitung jumlah label dengan masing-masing sentimennya
        label_counts = df_tweet['Sentiment_Type'].value_counts()

        # Menampilkan jumlah label dengan masing-masing sentimennya
        st.write("Jumlah label df_tweet dengan masing-masing sentimennya:")
        st.write(label_counts)

        # Menampilkan pie chart
        plt.figure(figsize=(8, 6))
        label_counts.plot(kind='pie', autopct='%1.1f%%')
        plt.title('Persentase Sentimen')
        plt.axis('equal')
        st.pyplot(plt)

        # Menghitung metrik evaluasi
        y_true = dt_tweet['label']
        y_pred = df_tweet['Sentiment_Type']

        accuracy = accuracy_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred, average='weighted')
        precision = precision_score(y_true, y_pred, average='weighted')
        f1 = f1_score(y_true, y_pred, average='weighted')

        accuracy_percent = round(accuracy * 100, 2)
        recall_percent = format(recall * 100, ".2f")
        precision_percent = format(precision * 100, ".2f")
        f1_percent = format(f1 * 100, ".2f")

        st.write("Accuracy (%):", accuracy_percent)
        st.write("Recall (%):", recall_percent)
        st.write("Precision score (%):", precision_percent)
        st.write("F1 score (%):", f1_percent)

if __name__ == '__main__':
    main()
