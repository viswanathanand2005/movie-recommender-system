import streamlit as st
import pickle

# ---------------- LOAD DATA ---------------- #
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- RECOMMENDER FUNCTION ---------------- #
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

# ---------------- STREAMLIT UI ---------------- #
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

st.title("🎬 Movie Recommender System")
st.write("Select a movie and get top 5 similar movies recommended for you!")

selected_movie = st.selectbox(
    "Search for a movie:",
    movies['title'].values
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("✨ Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        st.write(f"**{i}. {movie}**")
