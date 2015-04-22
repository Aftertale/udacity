import media
import fresh_tomatoes

#dictionary to store Movie information
movie_dict = {}

toy_story = media.Movie("Toy Story",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

pulp_fiction = media.Movie("Pulp Fiction",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

school_of_rock = media.Movie("School of Rock",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

snakes_on_a_plane = media.Movie("Snakes on a Plane",
                                "https://www.youtube.com/watch?v=vkckhcqiwM8")

django_unchained = media.Movie("Django Unchained",
                               "www.youtube.com/watch?v=eUdM9vrCbow")

princess_bride = media.Movie("The Princess Bride",
                             "www.youtube.com/watch?v=njZBYfNpWoE")

imitation_game = media.Movie("The Imitation Game",
                             "www.youtube.com/[todo:add]")

a_new_hope = media.Movie("Star Wars","www.youtube.com","1977")

unsorted_movies = []
for movie in movies:
    unsorted_movies.append(movie)
    
#unsorted_movies = [toy_story, avatar, school_of_rock, pulp_fiction, ratatouille, midnight_in_paris, snakes_on_a_plane, django_unchained, princess_bride, imitation_game, a_new_hope]
for movie in unsorted_movies:
    print(movie.title)
    info = movie.get_movie_info()
    movie.poster_image_url = info.get("Poster")
    movie.storyline = info.get("Plot").encode("utf-8").strip()
    movie.genre = info.get("Genre")
    movie.cast = info.get("Actors")
    movie.year = info.get("Year")
    movie.director = info["Director"]
movies = sorted(unsorted_movies, key=lambda movie: movie.title)


fresh_tomatoes.open_movies_page(movies)
