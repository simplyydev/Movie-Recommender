import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load movie data into a Pandas DataFrame
movies_df = pd.read_csv("movies.csv")

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(movies_df)

# Define a function to get the top n similar movies
def get_similar_movies(movie_title, n=10):
    # Get the index of the movie
    idx = movies_df[movies_df["title"] == movie_title].index[0]
    # Get the cosine similarity scores for all movies
    sim_scores = list(enumerate(cosine_sim[idx]))
    # Sort the movies by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    # Get the top n similar movies
    sim_scores = sim_scores[1:n+1]
    # Get the movie titles and indices
    movie_indices = [i[0] for i in sim_scores]
    movie_titles = movies_df.iloc[movie_indices]["title"].tolist()
    return movie_titles