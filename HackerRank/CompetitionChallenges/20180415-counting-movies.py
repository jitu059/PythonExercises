import sys
import os
import urllib2
import json

def getNumberOfMovies(substr):
    # Endpoint: "https://jsonmock.hackerrank.com/api/movies/search/?Title=substr"
    _url_to_contact = 'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + substr

    _response =  urllib2.urlopen(_url_to_contact)
    _json_data = json.load(_response)

    #print _json_data
    _r_nofmovies = 0
    try:
        _r_nofmovies = int(_json_data["total"])
    except:
        _r_nofmovies = 0
    finally:
        return _r_nofmovies



try:
    _substr = raw_input()
except:
    _substr = None

res = getNumberOfMovies(_substr)
print res
