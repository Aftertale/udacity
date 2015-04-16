import urllib2
import simplejson

url = "http://www.omdbapi.com/?t=ratatouille&y=&plot=full&r=json"

if __name__ == "__main__":
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    json = simplejson.load(f)
    print json
    print json.get('title')
    for item in json:
        print item.get('title')
