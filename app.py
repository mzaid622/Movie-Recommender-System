import streamlit as st
import pickle
import pandas as pd
import requests

# URLs for your pickle files
movies_url = "https://drive.google.com/file/d/1v216uBJrsaQIYRN1S2lWEq2m5mlXPRqk/view?usp=sharing"
similarity_url = "https://drive.google.com/file/d/1sYb6BpvZz7_brWjk2K547VjM3CY7QUxg/view?usp=sharing"

# Download movies_dict.pkl
response = requests.get(movies_url)
with open("movies_dict.pkl", "wb") as f:
    f.write(response.content)

# Download similarity.pkl
response = requests.get(similarity_url)
with open("similarity.pkl", "wb") as f:
    f.write(response.content)

# Load files
movies = pd.DataFrame(pickle.load(open("movies_dict.pkl", "rb")))
similarity = pickle.load(open("similarity.pkl", "rb"))


# ------------------ Fetch Poster Function ------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c6267fe6154692614ab558f87f27d080&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')  # Safe access
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        full_path = "https://via.placeholder.com/500x750?text=No+Image"
    return full_path

# ------------------ Recommendation Function ------------------
def recommendations(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend = []
    movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]]["movie_id"]  # Use TMDB movie ID
        recommend.append(movies.iloc[i[0]]["title"])
        movie_posters.append(fetch_poster(movie_id))

    return recommend, movie_posters

# ------------------ Load Data ------------------
movie_dict = pickle.load(open("./movies_dict.pkl", "rb"))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open("./similarity.pkl", "rb"))

# ------------------ Streamlit UI ------------------
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox("Select a Movie:", movies["title"].values)

if st.button("Recommend"):
    names, posters = recommendations(selected_movie)
    
    #Create columns for horizontal layout
    cols = st.columns(5)  # 5 recommendations
    for col, name, poster in zip(cols, names, posters):
        col.subheader(name)
        col.image(poster, width=150)  # Smaller width
