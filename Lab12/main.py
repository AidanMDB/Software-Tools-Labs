# ######################################################
# Author :  Aidan Dannhausen-Brun
# email :   adannhau@purdue.edu
# ID :      ee364a10
# Date :    4/7/24
# ######################################################


import flask
import time
import googlemaps
from pprint import pprint as pp
import csv
import datetime
# import sqlite3
# import hashlib


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


# pp(dir(gmaps))     will print out every function/thing we can use with googlemaps

API_KEY = "" # should be filled with a string of random letters and numbers from the google API

gmaps = googlemaps.Client(key=API_KEY)
app = flask.Flask(__name__)


def find_10_results(nearby):
    #pp(nearby)
    photo_num = -1
    places_10 = []
    for i, result in enumerate(nearby['results']):
        if result['rating'] >= 4 and result['user_ratings_total'] < 300:
            places_10.append({'name': result['name'], 'rating': result['rating']})

            if len(places_10) <= 3:
                photo = gmaps.places_photo(result['photos'][0]['photo_reference'], 400, 400)
                photo_num += 1
                with open(f'static/photo{photo_num}.jpeg', 'wb') as f:
                    for row in photo:
                        f.write(row)
        

        if len(places_10) == 10:
            break
    
    return places_10


def find_instr_dir(direction):
    directions = []
    for step in direction[0]['legs'][0]['steps']:
        directions.append({'instruction': step['html_instructions'], 'distance': step['distance']['text']})

    return directions


def create_csv(directions, results):
    with open('result_file.csv', 'w') as f:
        csv_writer = csv.writer(f)
        
        header = ['instruction', 'distance']
        csv_writer.writerow(header)
        for step in directions[0]['legs'][0]['steps']:
            #pp(step)
            dir_instr_list = [step['html_instructions'], step['distance']['text']]
            csv_writer.writerow(dir_instr_list)
        
        header = []
        csv_writer.writerow(header)
        header = ['name', 'rating']
        csv_writer.writerow(header)
        for result in results:
            name_rate_list = [result['name'], result['rating']]
            csv_writer.writerow(name_rate_list)


def getETA(directions):
    return directions[0]['legs'][0]['duration']['value']


@app.route('/', methods=['GET'])
def route():
    return flask.redirect('/home')


@app.route('/home', methods=['GET'])
def home():
    return flask.render_template('home.html')


@app.route('/home', methods=['POST'])
def submit_locs():
    origin = flask.request.form['input_origin']
    destination = flask.request.form['input_destination']
    date = flask.request.form['locTime']
    local_time = datetime.datetime.fromtimestamp(float(date))
    
    now=time.time()

    try:
        direction_results = gmaps.directions(origin, destination, mode='walking', departure_time=now)
    except Exception:
        return flask.redirect('/home')

    latitude = direction_results[0]['legs'][0]['end_location']['lat']
    longitude = direction_results[0]['legs'][0]['end_location']['lng']
    seconds_eta = getETA(direction_results)

    nearby_places = gmaps.places(location = f"{latitude}, {longitude}", radius=100, open_now=False, type='restaurant')
    #gmaps.places_photos()
    top_10 = find_10_results(nearby_places)
    dir = find_instr_dir(direction_results)
    create_csv(direction_results, top_10)


    local_tim_end = datetime.timedelta(seconds=seconds_eta)
    local_tim_end = local_tim_end + local_time
    date_time = local_tim_end.strftime("%m/%d/%Y, %H:%M:%S")
    #pp(nearby_places)

    return flask.render_template('results.html', nearby_locs=top_10, instr_dist=dir, eta=date_time)


@app.route('/results', methods=['POST'])
def download():
    return flask.send_from_directory(path='', directory='',filename='result_file.csv')


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == '__main__':
    app.run(port=8051, host='127.0.0.1', debug=True, use_evalex=False)
