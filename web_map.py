import folium
map = folium.Map(location = [52.06, 19.29], zoom_start = 6, tiles = "Stamen Terrain")
map.save("map.html")