import webbrowser
import re
import urllib2
import simplejson
        
class Movie():
    """This Class provides a way to store movie related information"""
    
    def __init__(self, movie_title, trailer_youtube):
        self.title = movie_title
##        self.storyline = movie_storyline
##        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
##        self.genre = genre
##        self.director = director
##        self.cast = cast

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_movie_info(self):
        url = "http://www.omdbapi.com/?t=" + self.title.replace(" ", "+") + "&y=&plot=full&r=json&tomatoes=true"
        req = urllib2.Request(url)
        opener = urllib2.build_opener()
        f = opener.open(req)
        json = simplejson.load(f)
        return(json)
    
    #def get_you_tube_link(self):
    #    youtubeurl = "https://gdata.youtube.com/feeds/api/videos"
