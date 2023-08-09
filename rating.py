# Define a function to get the average rating for a movie
def get_movie_rating(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/rating"
    response = requests.get(url, headers=headers)
    rating = response.json()["average_rating"]
    return rating

# Define a function to allow users to rate a movie
def rate_movie(movie_id, rating):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/rating"
    data = {
        "value": rating
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code

# Define a function to allow users to review a movie
def review_movie(movie_id, review):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"
    data = {
        "content": review
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code