# 🎬 Movie Recommender System  

A content-based **Movie Recommender System** built using **Python, Scikit-learn, and Streamlit**.  
This project suggests top 5 similar movies based on the movie selected by the user.  

---

## 🚀 Features  
- Clean separation of **model logic** and **UI**.  
- Uses **cosine similarity** on movie metadata (`overview`, `genres`, `keywords`, `cast`, `crew`).  
- Preprocessed data stored in **pickle files** for fast loading.  
- Interactive **Streamlit frontend**.  
- Easy to extend with movie posters (TMDB API).  

---

## 📂 Project Structure  
```
.
├── model.py          # Preprocesses data & saves movies + similarity into pickle files
├── app.py            # Streamlit frontend (loads pickle, provides UI)
├── tmdb_5000_movies.csv   # Dataset (Kaggle)
├── tmdb_5000_credits.csv  # Dataset (Kaggle)
├── movies.pkl        # Pickled dataframe (generated after running model.py)
├── similarity.pkl    # Pickled similarity matrix (generated after running model.py)
└── README.md         # Project documentation
```

---

## ⚙️ Installation  

### 1. Clone the repo & move into folder:
```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Download the dataset  
- [TMDB 5000 Movies Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)  
- Place `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` in the project folder.  

---

## ▶️ Usage  

### Step 1 – Run preprocessing (generate pickle files):
```bash
python model.py
```

### Step 2 – Launch the Streamlit app:
```bash
streamlit run app.py
```

### Step 3 – Interact 🎉  
- Select a movie from the dropdown.  
- Get top 5 recommended movies.  

---

## 📸 Demo Screenshot (example)  
*(You can add a screenshot later)*  
```
🎬 Movie Recommender System
Select a movie: [Avengers: Endgame]
✨ Recommended Movies:
1. Iron Man
2. Avengers: Infinity War
3. Captain America: Civil War
...
```

---

## 📌 Future Improvements  
- Show **movie posters** using TMDB API.  
- Add **search bar with autocomplete**.  
- Deploy on **Streamlit Cloud** or **Heroku**.  

---

## 📝 Author  
Developed by **Viswanath Anand** 💻  
