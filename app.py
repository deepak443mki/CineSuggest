import streamlit as st
from model import recommend_movie

st.set_page_config(page_title="CineSuggest 🎬", layout="centered")

st.title("🎬 CineSuggest")
st.subheader("A Smart Movie Recommender App")

st.markdown("Enter the name of a movie, and CineSuggest will recommend similar ones based on genres, popularity, and rating.")

movie_input = st.text_input("Enter a movie name:")

if st.button("Recommend"):
    if movie_input:
        results = recommend_movie(movie_input)
        if results[0] == "Movie not found.":
            st.warning("Sorry, we couldn't find that movie. Try another one.")
        else:
            st.success("Recommended Movies:")
            for i, movie in enumerate(results, 1):
                st.markdown(f"**{i}.** {movie}")
    else:
        st.info("Please enter a movie name.")
