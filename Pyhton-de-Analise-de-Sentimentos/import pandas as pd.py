import pandas as pd
import pyodbc
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon') # script de análise de sentimento 


def get_db_connection(): # conexão com o sevidor SQL
    conn_str = (
        "Driver={SQL Server};"
        "Server=DESKTOP-0KMVJ8E\\SQLEXPRESS;"
        "Database=MarketingAnalyticsProject;"
        "Trusted_Connection=yes;"
    )
    return pyodbc.connect(conn_str)

# função para buscar dados do SQL
def fetch_data_from_sql():
    query = "SELECT ReviewID, CustomerID, ProductID, ReviewDate, Rating, ReviewText FROM dbo.customer_reviews"
    with get_db_connection() as conn:
        return pd.read_sql(query, conn)


sia = SentimentIntensityAnalyzer()

# função para calcular o sentimento a partir do Vader
def calculate_sentiment(review):
    return sia.polarity_scores(review)['compound']

# categirização do sentimento
def categorize_sentiment(score, rating):
    if score > 0.05:
        return 'Positive' if rating >= 4 else 'Mixed Positive' if rating == 3 else 'Mixed Negative'
    elif score < -0.05:
        return 'Negative' if rating <= 2 else 'Mixed Negative' if rating == 3 else 'Mixed Positive'
    else:
        return 'Positive' if rating >= 4 else 'Negative' if rating <= 2 else 'Neutral'

# agrupando os sentimentos em faixas de valores (buckets)
def sentiment_bucket(score):
    if score >= 0.5:
        return '0.5 to 1.0'
    elif 0.0 <= score < 0.5:
        return '0.0 to 0.49'
    elif -0.5 <= score < 0.0:
        return '-0.49 to 0.0'
    else:
        return '-1.0 to -0.5'

# Buscar dados do SQL
customer_reviews_df = fetch_data_from_sql()

# Calcular o sentimento, categorizar e agrupar em buckets
customer_reviews_df['SentimentScore'] = customer_reviews_df['ReviewText'].apply(calculate_sentiment)
customer_reviews_df['SentimentCategory'] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(row['SentimentScore'], row['Rating']), axis=1)
customer_reviews_df['SentimentBucket'] = customer_reviews_df['SentimentScore'].apply(sentiment_bucket)

# Exibir as primeiras linhas do DataFrame
print(customer_reviews_df.head())

# Salvar o DataFrame em um arquivo CSV
customer_reviews_df.to_csv('fact_customer_reviews_with_sentiment.csv', index=False)