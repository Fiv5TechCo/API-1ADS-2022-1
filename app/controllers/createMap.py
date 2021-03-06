from geopy.geocoders import Nominatim
import os
import folium

def createMap(c):
  city = c
  loc = Nominatim(user_agent="GetLoc")
  getLoc = loc.geocode(city)

  m = folium.Map(location=[getLoc.latitude, getLoc.longitude], zoom_start=12)

  folium.Marker(location=[getLoc.latitude, getLoc.longitude],
                popup=(f"Vagas em {city}"),
                icon=folium.Icon(color='red', icon='info-sign')
                ).add_to(m)

  m.save(os.path.join('app/static/pages', 'map.html')) 