import streamlit as st
    
def main():
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Pendeteksi Kata Slang</p>', unsafe_allow_html=True)

    # Menambahkan penjelasan mengenai aplikasi
    st.markdown("""
    
Aplikasi ini adalah program Python yang menggunakan library Streamlit, Pandas, NLTK, dan beberapa library lainnya. Aplikasi ini digunakan untuk melakukan preprocessing pada teks dan mendeteksi kata-kata tidak baku. Beberapa fitur yang tersedia di aplikasi ini antara lain:

    a. User mengunggah file kamus KBBI dalam format CSV, TXT, XLS, atau XLSX.
    b. User mengunggah file data yang akan diproses dalam format CSV.
    c. Sistem melakukan preprocessing pada teks, termasuk penghapusan URL, mention, dan hashtag, serta tanda baca dan karakter non-ASCII.
    d. Sistem mencari kata slang dalam teks berdasarkan kamus KBBI.
    e. Sistem menghapus kata-kata berimbuhan dalam teks.
    f. Sistem menampilkan hasil preprocessing dan kata-kata tidak baku.
    g. User bisa mengeskpor kata slang ke file teks (TXT) atau file CSV.

    """)
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Optimalisasi Pra-proses</p>', unsafe_allow_html=True)

    # Menambahkan penjelasan mengenai aplikasi
    st.markdown("""
Fitur lainnya yang tersedia pada aplikasi ini adalah optimalisasi praproses, Praproses diperlukan untuk melakukan handling terhadap dataset yang dimiliki supaya data dapat sesuai dengan format yang diharapkan untuk pemrosesan lebih lanjut. Adapun langkah-langkah yang dapat ditempuh saat melakukan optimalisasi praproses ialah sebagai berikut:
                
    a. User mengunggah file yang akan dilakukan praproses dalam format CSV.
    b. Aplikasi akan menjalankan serangkaian tahapan praproses.
    C. Aplikasi akan meminta user agar menambahkan kamus slang dalam format TXT agar dapat melajutkan praproses.
    d. User mengunggah kamus slang dalam format TXT.
    e. Aplikasi akan menjalankan serangkaian tahapan praproses.
    f. Aplikasi akan meminta user untuk menambahkan kamus stopword dalam format TXT
    g. User menambahkan kamus stopword dalam format TXT.
    h. Praproses dilanjutkan hingga selesai.
    i. User dapat menekspor hasil praproses dalam format CSV atau XLSX.
                
    """)
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Analisis Sentimen Menggunakan InSet</p>', unsafe_allow_html=True)

    # Menambahkan penjelasan mengenai aplikasi
    st.markdown("""
Aplikasi ini adalah program Python yang menggunakan library Streamlit, Pandas, NLTK, dan beberapa library lainnya. Aplikasi ini digunakan untuk melakukan analisis sentimen menggunakan InSet. Beberapa fitur yang tersedia di aplikasi ini antara lain:
                
    a. Memuat kamus positif dan negatif: Program memungkinkan pengguna untuk mengunggah file positive.csv dan negative.csv menggunakan st.file_uploader(). Setelah file-file tersebut diunggah, fungsi load_lexicon() akan digunakan untuk memuat kamus positif dan negatif dari file-file tersebut.
    b. Memuat file CSV untuk analisis sentimen: Program memungkinkan pengguna untuk mengunggah file CSV yang akan dianalisis sentimen menggunakan st.file_uploader(). Jika file tersebut diunggah, file CSV akan dibaca dan dimasukkan ke dalam DataFrame menggunakan pd.read_csv().
    c. Analisis sentimen menggunakan kamus: Program melakukan analisis sentimen pada teks yang ada dalam file CSV. Jika kolom 'tweet_clean' ada dalam DataFrame, analisis sentimen akan dilakukan pada kolom 'tweet_clean'. Jika kolom tersebut tidak ada, analisis sentimen akan dilakukan pada kolom 'text_clean'.
    d. Menampilkan hasil analisis sentimen: Program menampilkan hasil analisis sentimen dalam bentuk jumlah polaritas positif, negatif, dan netral menggunakan st.write(). Hasil ini memberikan gambaran umum tentang sebaran sentimen dalam data.
    e. Menampilkan sampel teks dan polaritas: Program menampilkan sampel teks dari setiap label sentimen (negatif, positif, netral) beserta nilai polaritas menggunakan st.subheader() dan st.write(). Ini memungkinkan pengguna untuk melihat contoh teks dengan nilai polaritas terkait.
    f. Export ke CSV dan XLSX: Program menyediakan tombol untuk mengexport hasil analisis sentimen ke dalam file CSV dan XLSX menggunakan st.button(). Jika tombol tersebut ditekan, DataFrame yang telah dianalisis akan disimpan ke dalam file CSV atau XLSX menggunakan to_csv() atau to_excel().

    """)
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Analisis Sentimen Menggunakan Vader</p>', unsafe_allow_html=True)

    # Menambahkan penjelasan mengenai aplikasi
    st.markdown("""
Aplikasi ini adalah program Python yang menggunakan library Streamlit, Pandas, NLTK, dan beberapa library lainnya. Aplikasi ini digunakan untuk melakukan analisis sentimen menggunakan Vader. Beberapa fitur yang tersedia di aplikasi ini antara lain:
                
    a. Upload File: Aplikasi memungkinkan pengguna untuk mengunggah file dalam format xlsx yang berisi teks yang akan dianalisis sentimennya.
    b. Analisis Sentimen: Aplikasi melakukan analisis sentimen pada setiap teks yang ada dalam file xlsx menggunakan Sentiment Intensity Analyzer (SIA) dari NLTK (Natural Language Toolkit). Setiap teks diberikan skor sentimen dalam bentuk compound score, negative score, neutral score, dan positive score.
    c. Menambahkan Skor Sentimen ke DataFrame: Setelah melakukan analisis sentimen, aplikasi menambahkan skor sentimen ke dalam DataFrame yang mengandung teks yang telah dianalisis. Skor sentimen ditambahkan sebagai kolom baru dalam DataFrame.
    d. Menampilkan DataFrame: Aplikasi menampilkan DataFrame yang berisi teks yang telah dianalisis beserta skor sentimennya. DataFrame ditampilkan menggunakan Streamlit.
    e. Menyimpan Skor Sentimen ke dalam File CSV: Aplikasi menyimpan skor sentimen ke dalam file CSV dengan nama "Hasil vader.csv". Setiap skor sentimen disimpan dalam baris terpisah dengan kolom-kolom yang menyatakan compound, negative, neutral, dan positive score.
    f. Menampilkan Diagram Hasil Analisis Sentimen: Aplikasi menampilkan diagram lingkaran (pie chart) yang menunjukkan distribusi sentimen berdasarkan skor sentimen yang diperoleh. Diagram ini menunjukkan persentase sentimen positif, negatif, dan netral dalam teks yang dianalisis.
    """)
    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Evaluasi Matrix InSet</p>', unsafe_allow_html=True)

    # Menambahkan penjelasan mengenai aplikasi
    st.markdown("""
Aplikasi ini adalah program Python yang menggunakan library Streamlit dan Pandas untuk melakukan evaluasi matrix InSet pada data hasil analisis sentimen:

    a. Mengunggah file sebelum analisis sentimen dan sesudah analisis sentimen: User dapat memilih file yang akan diunggah untuk dievaluasi matrixnya.
    b. Menampilkan data asli: Sistem menampilkan data sebelum analisis sentimen dan sesudah analisis sentimen yang sudah dimasukan.
    c. Menampilkan distribusi label pada data asli: Sistem menampilkan grafik pie yang menunjukkan distribusi label pada data sebelum analisis sentimen.
    d. Menampilkan distribusi sentimen pada data hasil analisis: Sistem menampilkan grafik pie yang menunjukkan distribusi sentimen pada data sesudah analisis sentimen.
    e. Menghitung evaluasi matrix weighted-average: Sistem menghitung dan menampilkan evaluasi matrix seperti akurasi, recall, presisi, dan F1 score untuk analisis sentimen menggunakan matrix weighted.
    f. Menampilkan evaluasi matrix weighted-average dalam persentase: Sistem menampilkan evaluasi matrix seperti akurasi, recall, presisi, dan F1 score dalam bentuk persentase.
    g. Menghitung evaluasi matrix macro-average: Sistem menghitung dan menampilkan evaluasi matrix seperti akurasi, recall, presisi, dan F1 score untuk analisis sentimen menggunakan matrix macro-averaged.
    h. Menampilkan evaluasi matrix macro-average dalam persentase: Sistem menampilkan evaluasi matrix seperti akurasi, recall, presisi, dan F1 score dalam bentuk persentase.

    """)

    st.markdown('<p style="font-family: Times New Roman; font-size: 32px; font-weight: bold;">Evaluasi Matrix Vader</p>', unsafe_allow_html=True)

    # Menambahkan penjelasan mengenai aplikasi
    st.markdown("""
Aplikasi ini adalah program Python yang menggunakan library Streamlit dan Pandas untuk melakukan evaluasi matrix Vader pada data hasil analisis sentimen:

    a. Upload File: Aplikasi memungkinkan pengguna untuk mengunggah dua file dalam format CSV, yaitu dt_tweet dan df_tweet.
    b. Menampilkan Dataframe: Aplikasi menampilkan isi dari dt_tweet dan df_tweet setelah file-file tersebut diunggah.
    c. Mengubah Label: Aplikasi mengubah label pada dt_tweet dengan menggantinya menggunakan mapping dictionary. Label-label yang semula dalam bentuk teks ("neutral", "positive", "negative") diubah menjadi nilai numerik (0, 1, -1).
    d. Menambahkan Kolom Baru: Aplikasi menambahkan kolom baru pada df_tweet dengan nama "Sentiment_Type". Nilai pada kolom ini ditentukan berdasarkan nilai pada kolom "Compound". Jika nilai "Compound" >= 0.05, maka nilai pada "Sentiment_Type" menjadi "Positive". Jika nilai "Compound" <= -0.05, maka nilai pada "Sentiment_Type" menjadi "Negative". Jika nilai "Compound" berada di antara -0.05 dan 0.05, maka nilai pada "Sentiment_Type" menjadi "Neutral".
    e. Menampilkan Pie Chart: Aplikasi menampilkan pie chart yang menunjukkan persentase sentimen pada dt_tweet dan df_tweet. Pie chart ini menggambarkan distribusi sentimen dalam bentuk persentase.
    f. Menghitung Metrik Evaluasi: Aplikasi menghitung metrik evaluasi seperti akurasi (accuracy), recall, presisi (precision), dan F1-score. Metrik evaluasi ini dihitung dengan membandingkan label yang ada pada dt_tweet (sebagai label sebenarnya) dengan label yang ada pada df_tweet (sebagai label prediksi). Hasil metrik evaluasi ditampilkan dalam bentuk persentase.
    """)
if __name__ == "__main__":
    main()