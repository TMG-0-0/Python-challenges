# Create a dictionary of your favorite movies and their release years. Add a new movie to the dictionary, update the release year of one of the movies, and then remove a movie.

fav_movies = {
    'The Dark Knight': '2008',
    'The Godfather': '1972',
    'Fight Club': '2000',
    'The Conjuring': '2013'
    }
fav_movies['The Avengers'] = '2012'
fav_movies['Fight Club'] = '1999'
fav_movies.pop('The Conjuring')

print(fav_movies)