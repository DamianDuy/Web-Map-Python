import folium
import pandas

class Webmap:
    def __init__(self):
       self.dataVis = pandas.read_csv("visited.txt")
       self.latitVis = list(self.dataVis["LAT"])
       self.longiVis = list(self.dataVis["LON"])
       self.nameVis = list(self.dataVis["NAME"])
       self.rates = list(self.dataVis["RATE"])

       self.dataUnvis = pandas.read_csv("to_visit.txt")
       self.latitUnvis = list(self.dataUnvis["LAT"])
       self.longiUnvis = list(self.dataUnvis["LON"])
       self.nameUnvis = list(self.dataUnvis["NAME"])

       self.min_popul = 15000000
       self.mid_popul = 25000000

       self.map = folium.Map(location = [52.06, 19.29], zoom_start = 6, tiles = "Stamen Terrain")
       self.fgVis = folium.FeatureGroup(name = "Visited Markers")
       self.fgUnvis = folium.FeatureGroup(name = "Unvisited Markers")
       self.fgPopul = folium.FeatureGroup(name = "Population Layer")
    
    @staticmethod
    def colouring(rate):
       extrRate = rate[0] + rate[1]
       if extrRate == "10":
           return "blue"
       else:
           return "green"    

    @staticmethod
    def iconing(rate):
       extrRate = rate[0] + rate[1]
       if extrRate == "10":
           return "heart-o"
       else:
           return "check-circle-o"
    
    def creatingMarkers(self):
       for lat, lon, nam, rat in zip(self.latitVis, self.longiVis, self.nameVis, self.rates):
           self.fgVis.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(str(nam) + "\n" + str(rat), parse_html = True), icon = folium.Icon(color = Webmap.colouring(rat), icon = Webmap.iconing(rat), prefix = "fa")))
       for lat, lon, nam in zip(self.latitUnvis, self.longiUnvis, self.nameUnvis):
           self.fgUnvis.add_child(folium.Marker(location = [lat, lon], popup = folium.Popup(str(nam), parse_html = True), icon = folium.Icon(color = "red", icon = "clock-o", prefix = "fa"))) 
    
    def creatingPopulLayer(self):
        self.fgPopul.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read(), style_function = lambda x: {"fillColor" : "green" if x["properties"]["POP2005"] < self.min_popul else "yellow" if self.min_popul <= x["properties"]["POP2005"] < self.mid_popul else "red"}))

    def mapAdd(self):
        self.map.add_child(self.fgVis)
        self.map.add_child(self.fgUnvis)
        self.map.add_child(self.fgPopul)
        self.map.add_child(folium.LayerControl())
        self.map.save("map.html")

def main():
    visMap = Webmap()
    visMap.creatingMarkers()
    visMap.creatingPopulLayer()
    visMap.mapAdd()

if __name__ == "__main__":
    main()