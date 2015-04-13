import webbrowser
import re
import urllib2
import demjson
import simplejson
        
class Movie():
    """This Class provides a way to store movie related information"""
    
    def __init__(self, movie_title, trailer_youtube):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube
        self.storyline = "Plot Synopsis has not been found!"
        self.rating = "rating unknown"
        self.poster_image_url = "image not found!"
        self.genre = "genre unknown!"


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_movie_info(self):
        url = "http://www.omdbapi.com/?t=" + self.title + "&y=&plot=full&r=json"
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        f = opener.open(req)
        json = simplejson.load(f)
        return(json)
    
