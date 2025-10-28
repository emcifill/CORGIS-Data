from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def popularity():
   
    artists = get_artist_options()
    #print(artists)
    return render_template('popularity.html', artist_options=artists)

@app.route('/showFact')
def render_fact():
    artists = get_artist_options()
    artist = request.args.get('artist')
    artisthotttnessss = get_artist_hotttnesss(artist)
    
    # county = county_most_under_18(artist)
    # county2 = county_most_population(artist)
    fact = artist + " popularity is"
    fact2 = artisthotttnessss
    return render_template('popularity.html', artist_options=artists, funFact=fact, funFact2=fact2)
    
def get_artist_options():
    """Return the html code for the drop down menu.  Each option is a artist abbreviation from the demographic data."""
    with open('music.json') as music_data:
        counties = json.load(music_data)
    artists=[]
    for c in counties:
        if c["artist"]["name"] not in artists:
            artists.append(c["artist"]["name"])
    options=""
    for s in artists:
        options += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options

def get_artist_hotttnesss(name):
    """Return the html code for the drop down menu.  Each option is a artist abbreviation from the demographic data."""
    with open('music.json') as music_data:
        counties = json.load(music_data)
   
    for c in counties:
        if c["artist"]["name"] == name:
           return c["artist"]["hotttnesss"]



def artistdata():
   
    artists2 = get_artist_options2()
    #print(artists)
    return render_template('data.html', artist_options2=artists2)

@app.route('/showFact')
def render_fact2():
    artists2 = get_artist_options2()
    artist2 = request.args.get2('artist')
    artisthotttnessss2 = get_artist_hotttnesss2(artist2)
    
    # county = county_most_under_18(artist)
    # county2 = county_most_population(artist)
    fact3 = artist2 + " popularity is"
    fact4 = artisthotttnessss2
    return render_template('data.html', artist_options2=artists2, funFact3=fact3, funFact4=fact4)
    
def get_artist_options2():
    """Return the html code for the drop down menu.  Each option is a artist abbreviation from the demographic data."""
    with open('music.json') as music_data2:
        counties2 = json.load(music_data2)
    artists2=[]
    for c in counties2:
        if c["artist"]["name"] not in artists2:
            artists2.append(c["artist"]["name"])
    options2=""
    for s in artists2:
        options2 += Markup("<option value=\"" + s + "\">" + s + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options2

def get_artist_hotttnesss2(name2):
    """Return the html code for the drop down menu.  Each option is a artist abbreviation from the demographic data."""
    with open('music.json') as music_data2:
        counties2 = json.load(music_data2)
   
    for c in counties2:
        if c["artist"]["name"] == name2:
           return c["artist"]["hotttnesss"]
           
# def county_most_under_18(artist):
    # """Return the name of a county in the given artist with the highest percent of under 18 year olds."""
    # with open('music.json') as music_data:
       # # counties = json.load(music_data)
    # highest=0
    # county = ""
    # for c in counties:
        # if c["artist"]["hotttnesss"] == artist:
            # if c["artist"]["hotttnesss"] > highest:
                # highest = c["artist"]["hotttnesss"]
                # county = c["artist"]["hotttnesss"]
    # return county
    
    
# def county_most_population(artist):
    # """Return the name of a county in the given artist with the highest percent of under 18 year olds."""
    # with open('music.json') as music_data:
        # counties = json.load(music_data)
    # highest=0
    # county2 = ""
    # for c in counties:
        # if c["song"] == artist:
            # if c["hotttnesss"] > highest:
                # highest = c["hotttnesss"]
                # county2 = c["artist"]
    # return county2

def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url


if __name__ == '__main__':
    app.run(debug=True) # change to False when running in production