import folium
import pandas

dataVis = pandas.read_csv("visited.txt")
latitVis = list(dataVis["LAT"])
longiVis = list(dataVis["LON"])
nameVis = list(dataVis["NAME"])
rates = list(dataVis["RATE"])

dataUnvis = pandas.read_csv("to_visit.txt")
latitUnvis = list(dataUnvis["LAT"])
longiUnvis = list(dataUnvis["LON"])
nameUnvis = list(dataUnvis["NAME"])


map = folium.Map(location = [52.06, 19.29], zoom_start = 6, tiles = "Stamen Terrain")
fgVis = folium.FeatureGroup(name = "Visited Markers")
fgUnvis = folium.FeatureGroup(name = "Unvisited Markers")

for lat, lon, nam, rat in zip(latitVis, longiVis, nameVis, rates):
    fgVis.add_child(folium.Marker(location = [lat, lon], popup = str(nam) + "\n" + str(rat), icon = folium.Icon(color = 'green')))
for lat, lon, nam in zip(latitUnvis, longiUnvis, nameUnvis):
    fgUnvis.add_child(folium.Marker(location = [lat, lon], popup = str(nam), icon = folium.Icon(color = 'red')))

map.add_child(fgVis)
map.add_child(fgUnvis)
map.save("map.html")