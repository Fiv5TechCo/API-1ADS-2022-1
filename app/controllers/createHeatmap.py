from encodings import utf_8
from geopy.geocoders import Nominatim
import os
import folium
import json
import csv
from folium.plugins import HeatMap

citiesCoord = []
cities = []
coordinates = []
city = []

def createHeatmap():

    with open('app/models/latitude-longitude-cidades.csv', encoding='utf_8') as my_csv:
        citiesCoordinates = csv.reader(my_csv, delimiter=';')
        for i in citiesCoordinates:
            """ print(i) """
            citiesCoord.append([(f'{i[2]} / {i[1]}'), i[4], i[3]])

    with open('app/models/for_Metricas.json', encoding='utf_8') as my_json:
        data = json.load(my_json)
        for i in range(0, len(data)):
            place = data[i]['place'].split(',')
            if len(place) > 1:
                city = place[1][2:]
            else:
                city = place[0]
            cities.append(city)
    
    for city in sorted(cities):
        for coord in citiesCoord:
            if city == coord[0]:
                coordinates.append((coord[1], coord[2]))
            else:
                continue

    m = folium.Map([-15.779458, -47.939018], zoom_start=4)

    HeatMap(coordinates).add_to(m)

    m.save(os.path.join('app/static/pages', 'hmap.html')) 
