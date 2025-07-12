import streamlit as st
import pickle
import requests

#functions for fetching poster
def fetch_poster(movies_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=19b14193a2190d4e4e34415ee90f6fbc&language=en-US'.format(movies_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
#finction for the rocommend button which return image and name
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movies_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movies_id))
    return recommended_movies,recommended_movies_posters

movies = pickle.load(open('movies.pkl', 'rb'))#loading the pkl file for movies

similarity= pickle.load(open('similarity.pkl', 'rb'))#loading the pkl files for recommendation
st.title('Movie Recommender System')

#for search area
st.subheader("Hi, what Should I recommend For you!")
selected_movies = st.selectbox(
    " ",
    movies['title'].values,
)
#for button and output
if st.button("Recommend"):
    names,posters=recommend(selected_movies)
    st.subheader("My Top 5 Recommendations:",divider='red')
    col1, col2, col3 ,col4, col5 = st.columns(5, border=True,vertical_alignment="top")
    

    with col1:

        st.image(posters[0])
        st.text(names[0])

    with col2:
        
        st.image(posters[1])
        st.text(names[1])
    
    with col3:
        
        st.image(posters[2])
        st.text(names[2])
        
    with col4:
        st.image(posters[3])
        st.text(names[3])
        
    with col5:
        
        st.image(posters[4])
        st.text(names[4])
