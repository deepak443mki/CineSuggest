import streamlit as st
import pandas as pd
import ast
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

@st.cache_data
def load_data():
    df = pd.read_csv("movies_metadata.csv", low_memory=False)
    movies = df[['title', 'genres', 'vote_average', 'popularity']].copy()
    movies = movies.dropna(subset=['genres', 'vote_average', 'popularity'])

    def parse_genres(genre_str):
        try:
            genres = [d['name'] for d in ast.literal_eval(genre_str)]
        except:
            genres = []
        return genres

    movies['genres'] = movies['genres'].apply(parse_genres)
    scaler = MinMaxScaler()
    movies[['vote_average', 'popularity']] = scaler.fit_transform(movies[['vote_average', 'popularity']])
    kmeans = KMeans(n_clusters=10, random_state=42)
    movies['cluster'] = kmeans.fit_predict(movies[['vote_average', 'popularity']])
    return movies

movies = load_data()

def recommend_movie(title):
    title = title.lower().strip()
    if title not in movies['title'].str.lower().values:
        return ["Movie not found."]
    
    idx = movies[movies['title'].str.lower() == title].index[0]
    cluster = movies.loc[idx, 'cluster']
    genres = set(movies.loc[idx, 'genres'])

    cluster_movies = movies[movies['cluster'] == cluster].copy()
    cluster_movies['score'] = cluster_movies['genres'].apply(lambda g: len(set(g).intersection(genres)))
    cluster_movies = cluster_movies.sort_values(by='score', ascending=False)

    return cluster_movies[cluster_movies.index != idx]['title'].head(5).tolist()

