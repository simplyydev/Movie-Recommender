import requests

# Obtain an API key from the TMDB website
api_key = "3adf352eca0a837e90c0a3801c448790"

# Use the API key to authenticate your requests to the TMDB API
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json;charset=utf-8"
}

# Set up the necessary endpoints to fetch movie data
def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_movie_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    response = requests.get(url, headers=headers)
    return response.json()

def get_movie_ratings(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/rating"
    response = requests.get(url, headers=headers)
    return response.json()