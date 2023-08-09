# Define a function to search for movies by keyword
def search_movies(query):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": query
    }
    response = requests.get(url, headers=headers, params=params)
    results = response.json()["results"]
    movies = []
    for result in results:
        movie = {
            "id": result["id"],
            "title": result["title"],
            "poster_path": f"https://image.tmdb.org/t/p/w500{result['poster_path']}"
        }
        movies.append(movie)
    return movies

# Define a function to filter movies by genre
def filter_movies_by_genre(genre_id):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": api_key,
        "with_genres": genre_id
    }
    response = requests.get(url, headers=headers, params=params)
    results = response.json()["results"]
    movies = []
    for result in results:
        movie = {
            "id": result["id"],
            "title": result["title"],
            "poster_path": f"https://image.tmdb.org/t/p/w500{result['poster_path']}"
        }
        movies.append(movie)
    return movies