import webbrowser
import urllib
import movie
import demjson
import simplejson


#get_movie_info(movie_title)
#movies = {"Toy Story": "https://www.youtube.com/watch?v=KYz2wyBy3kc", "Avatar", "Pulp Fiction", "Snakes on a Plane", "Star Wars", "Guardians of the Galaxy"}

#for item in movies:
#    item = item.replace(" ", "-")
#    item = movie.Movie(movie_title, trailer_youtube)
    

toy_story = movie.Movie("Toy+Story", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
info = toy_story.get_movie_info()
print info
toy_story.storyline = info.get("Plot")
print toy_story.storyline
