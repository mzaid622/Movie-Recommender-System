# 🎬 CineMatch – Movie Recommender System

**CineMatch** is an intelligent movie recommendation web application built with **Streamlit** that suggests similar movies using a **Content-Based Filtering** approach powered by machine learning.  
It helps users discover new movies based on their favorite films by analyzing **genres, cast, crew, keywords, and plot similarities**.

---

## 🌐 Live Demo
👉 **[Launch the App:](https://movierecommender622.streamlit.app/)** 

---

## 🧠 Model Overview
The **Content-Based Filtering** algorithm recommends movies by analyzing their **content features** rather than user ratings. It works by:

1. Converting movie features (genres, cast, keywords, overview) into numerical vectors using **Bag of Words**
2. Calculating similarity between movies using **Cosine Similarity**
3. Recommending the **top 5 most similar movies** based on the selected film

---

## ⚙️ Features

- 🎥 Recommends **5 similar movies** based on content similarity  
- 🖼️ Displays **movie posters** fetched from **TMDB API**  
- 📊 Interactive and responsive **Streamlit interface**  
- 🧮 Powered by **NLP** and **Machine Learning** techniques  
- 🔍 Search from **4,806 movies database**  
- ⚡ **Instant prediction results**

---

## 📋 Dataset Information
The dataset used for model training includes comprehensive movie details from the **TMDB 5000 Movie Dataset**.

| Feature | Description |
|----------|--------------|
| **Movie ID** | Unique identifier |
| **Title** | Movie name |
| **Genres** | Movie categories (Action, Drama, etc.) |
| **Keywords** | Plot-related keywords |
| **Cast** | Top 3 actors |
| **Crew** | Director name |
| **Overview** | Plot summary |

**Total Movies:** 4,806 (after preprocessing)

---

## 📊 Model Performance

| Component | Details |
|------------|----------|
| **Algorithm** | Content-Based Filtering |
| **Vectorization** | Bag of Words (5000 features) |
| **Similarity Metric** | Cosine Similarity |
| **Text Processing** | Porter Stemming, Stop Words |
| **Dataset Size** | 4,806 movies |

---

## 🧰 Tech Stack

- 🐍 **Python 3.8+**
- 🌐 **Streamlit** – Web app framework  
- 🤖 **scikit-learn** – ML (CountVectorizer, cosine_similarity)  
- 🗣️ **NLTK** – NLP (PorterStemmer)  
- 📊 **pandas, NumPy** – Data handling  
- 🌎 **Requests** – TMDB API integration  
- 💾 **Pickle** – Model serialization  

---

## 💡 Future Improvements

- ➕ Add **collaborative filtering** approach  
- 🔄 Implement **hybrid recommendation system**  
- ⭐ Include **user ratings and reviews**    
- 🎨 Enhance **UI/UX** with advanced search filters  
- 🧭 Allow **genre-based filtering**  
- 📈 Add **trending and popular movies** section  

---

## 📁 Project Structure
├── app.py # Streamlit web application
├── Recommender_System.ipynb # Model training notebook
├── movies_dict.pkl # Processed movie data
├── similarity.pkl # Similarity matrix
└── README.md # Documentation


---

## 🧑‍💻 Author
**Muhammad Zaid**  
📍 Lahore, Punjab, PK  
💼 Machine Learning & Data Science Enthusiast  

> 💬 *"Building intelligent systems one movie at a time."*

---

⭐ **If you like this project, consider giving it a star on GitHub!**

