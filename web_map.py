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

def colouring(rate):
    extrRate = rate[0] + rate[1]
    if extrRate == "10":
        return "blue"
    else:
        return "green"    

def iconing(rate):
    extrRate = rate[0] + rate[1]
    if extrRate == "10":
        return "heart-o"
    else:
        return "check-circle-o" 


map = folium.Map(location = [52.06, 19.29], zoom_start = 6, tiles = "Stamen Terrain")
fgVis = folium.FeatureGroup(name = "Visited Markers")
fgUnvis = folium.FeatureGroup(name = "Unvisited Markers")

for lat, lon, nam, rat in zip(latitVis, longiVis, nameVis, rates):
    fgVis.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(str(nam) + "\n" + str(rat), parse_html = True), icon = folium.Icon(color = colouring(rat), icon = iconing(rat), prefix = "fa")))
for lat, lon, nam in zip(latitUnvis, longiUnvis, nameUnvis):
    fgUnvis.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(str(nam), parse_html = True), icon = folium.Icon(color = "red", icon = "clock-o", prefix = "fa")))

map.add_child(fgVis)
map.add_child(fgUnvis)
map.save("map.html")