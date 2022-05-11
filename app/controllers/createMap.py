from geopy.geocoders import Nominatim
import os # LIB DO PYTHON QUE ADICIONA COMANDOS DO SISTEMA OPERACIONAL, TALVEZ POSSA SER USADO PARA GERAR O ARQUIVO EM OUTRA PASTA (os.path.join...)
import folium

def createMap(c):
  city = c
  loc = Nominatim(user_agent="GetLoc")
  getLoc = loc.geocode(city)

  m = folium.Map(location=[getLoc.latitude, getLoc.longitude], zoom_start=15)

  folium.Marker(location=[getLoc.latitude, getLoc.longitude],
                popup=(f"Vagas em {city}"),
                icon=folium.Icon(color='red', icon='info-sign')
                ).add_to(m)

  m.save(os.path.join('app/static/pages', 'map.html'))