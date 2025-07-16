# CineSuggest
A smart movie recommendation system built with machine learning and Streamlit, recommending movies based on genre, popularity, and user preferences.

# Python Libraries Used
 pandas   -     Data loading, cleaning, manipulation      
 numpy    -    Numerical operations                      
 scikit-learn - ML model (clustering), data preprocessing 
 ast      -    Parsing stringified lists (for genres)    
 streamlit  -  Building the web-based UI                 

# Machine Learning Model Used
KMeans (from sklearn.cluster) - Clusters movies based on normalized vote_average and popularity to group similar types of movies

# Techniques and Concepts Used
Content-based filtering - Uses movie metadata (genres, rating, popularity) for recommendations
Clustering with KMeans - Groups movies into clusters based on popularity & rating similarity
Genre intersection scoring - Recommends movies with the most genre overlap within the same cluster
Feature scaling (MinMaxScaler) - Normalizes vote_average and popularity between 0 and 1
Text preprocessing - Lowercasing, trimming input for better matching
