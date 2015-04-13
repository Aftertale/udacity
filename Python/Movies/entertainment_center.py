import media
import fresh_tomatoes

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

unsorted_movies = [toy_story, avatar, school_of_rock, pulp_fiction, ratatouille, midnight_in_paris, snakes_on_a_plane, django_unchained]
for movie in unsorted_movies:
    print movie.title
    info = movie.get_movie_info()
    movie.poster_image_url = info.get("Poster")
    movie.storyline = info.get("Plot").encode("utf-8").strip()
    movie.genre = info.get("Genre")
    movie.cast = info.get("Actors")
    movie.year = info.get("Year")
movies = sorted(unsorted_movies, key=lambda movie: movie.title)


fresh_tomatoes.open_movies_page(movies)
