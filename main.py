import pandas
import web_map
from os import system, name

class Messages:
    @staticmethod
    def giveId():
        return "Give the ID of the place: "
    @staticmethod
    def giveNamePlace():
        return "Give the name of the place: "
    @staticmethod
    def giveNameCountry():
        return "Give the name of the country: "
    @staticmethod
    def giveRate():
        return "Rate the place out of 10: "
    @staticmethod
    def giveLat():
        return "Give the latitude: "
    @staticmethod
    def giveLong():
        return "Give the longitude: "
    @staticmethod
    def coorWrong():
        return "Coordinates must be numbers."
    @staticmethod
    def rateWrong():
        return "Rate must be a number between 0 and 10."
    @staticmethod
    def idNotNum():
        return "ID must be a number."
    @staticmethod
    def posNotExists():
        return "Position with the given ID does not exist."
    @staticmethod
    def noOptInMenu():
        return "Not such option in the menu."
    @staticmethod
    def ifSaveFiles():
        return "Do you wish to save? Type yes/no: "
    @staticmethod
    def saving():
        return "Saving..."
    @staticmethod
    def showMenu():
        print("1. Add marker to visited.")
        print("2. Add marker to unvisited.")
        print("3. Change marker to visited.")
        print("4. Delete marker from visited.")
        print("5. Delete marker from unvisited.")
        print("6. Exit")

class Data:
    def __init__(self):
       self.dataVis = pandas.read_csv("visited.txt")
       self.dataUnvis = pandas.read_csv("to_visit.txt")

    def addMarkerVis(self, dataVisual):
       print(Messages.giveNamePlace())
       name = input()
       print(Messages.giveNameCountry())
       country = input()
       print(Messages.giveRate())
       rateTem = input()
       print(Messages.giveLat())
       latitude = input()
       print(Messages.giveLong())
       longitude = input()
       if ifFloat(latitude) and ifFloat(longitude):
           latitude = float(latitude)
           longitude = float(longitude)
       else:
           print(Messages.coorWrong())
           return dataVisual        
       while not ifFloat(rateTem) or float(rateTem) not in range (0,11):
           print(Messages.rateWrong())
           print(Messages.giveRate())
           rateTem = input()  
       rate = rateTem + "/10"    
       idVis = list(dataVisual["ID"])
       if not idVis:
           i = 1
       else:
           i = idVis[-1] + 1        
       dfTem = pandas.DataFrame({"ID" : [i],
                                 "NAME": [name],
                                 "COUNTRY": [country],
                                 "RATE": [rate],
                                 "LAT": [latitude],
                                 "LON": [longitude]})
       return dataVisual.append(dfTem, ignore_index = True)

    def addMarkerUnvis(self, dataVisual):
       print(Messages.giveNamePlace())
       name = input()
       print(Messages.giveNameCountry())
       country = input()
       print(Messages.giveLat())
       latitude = input()
       print(Messages.giveLong())
       longitude = input()
       if ifFloat(latitude) and ifFloat(longitude):
           latitude = float(latitude)
           longitude = float(longitude)
       else:
           print(Messages.coorWrong())
           return dataVisual
       idUnVis = list(dataVisual["ID"])
       if not idUnVis:
           i = 1
       else:
           i = idUnVis[-1] + 1          
       dfTem = pandas.DataFrame({"ID" : [i],
                              "NAME": [name],
                              "COUNTRY": [country],
                              "LAT": [latitude],
                              "LON": [longitude]})
       return dataVisual.append(dfTem, ignore_index = True)

    def deleteMarker(self, dataVisual, id, ifShowMessage):
        ifExists = False
        if ifFloat(id):
            id = float(id)
        elif ifShowMessage:
            print(Messages.idNotNum())
            return dataVisual    
        for i in list(dataVisual["ID"]):
            if id == i:
                dataVisual.drop(dataVisual[dataVisual.ID == i].index, inplace = True)
                ifExists = True
        if not ifExists and ifShowMessage:
            print(Messages.posNotExists())
        return dataVisual

    def changeMarker(self, dataVisualVis, dataVisualUnvis, id):
        ifExists = False
        if ifFloat(id):
            id = float(id)
        else:
            print(Messages.idNotNum())
            return dataVisualVis
        idVis = list(dataVisualVis["ID"])    
        idUnvis = list(dataVisualUnvis["ID"])
        nameUnvis = list(dataVisualUnvis["NAME"])
        countryUnvis = list(dataVisualUnvis["COUNTRY"])
        latitUnvis = list(dataVisualUnvis["LAT"])
        longiUnvis = list(dataVisualUnvis["LON"])
        if not idVis:
            num = 1
        else:
            num = idVis[-1] + 1        
        for i, nam, coun, lat, lon in zip(idUnvis, nameUnvis, countryUnvis, latitUnvis, longiUnvis):
            if id == i:
                newName = nam
                newCountry = coun
                newLatitude = lat
                newLongitude = lon
                ifExists = True
        if not ifExists:
            print(Messages.posNotExists())
            return dataVisualVis
        print(Messages.giveRate())
        rateTem = input()    
        while not ifFloat(rateTem) or float(rateTem) not in range (0,11):
            print(Messages.rateWrong())
            print(Messages.giveRate())
            rateTem = input()  
        newRate = rateTem + "/10"    
        dfTem = pandas.DataFrame({"ID" : [num],
                                  "NAME": [newName],
                                  "COUNTRY": [newCountry],
                                  "RATE": [newRate],
                                  "LAT": [newLatitude],
                                  "LON": [newLongitude]})
        return dataVisualVis.append(dfTem, ignore_index = True)    

def clear():
    if name == "posix":
        _ = system("clear")
    else:
        _ = system("cls")

def ifFloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def main():
   data = Data ()
   ifSaveVis = False
   ifSaveUnvis = False
   choice = "0"
   while True:
       Messages.showMenu()
       choice = input()
       clear()
       if choice == "1":
           data.dataVis = data.addMarkerVis(data.dataVis)
           ifSaveVis = True
       elif choice == "2":
           data.dataUnvis = data.addMarkerUnvis(data.dataUnvis)
           ifSaveUnvis = True
       elif choice == "3":
           print(Messages.giveId())
           id = input()
           data.dataVis = data.changeMarker(data.dataVis, data.dataUnvis, id)
           data.dataUnvis = data.deleteMarker(data.dataUnvis, id, False)
           ifSaveVis = True
           ifSaveUnvis = True
       elif choice == "4":
           print(Messages.giveId())
           id = input()
           data.dataVis = data.deleteMarker(data.dataVis, id, True)
           ifSaveVis = True
       elif choice == "5":
           print(Messages.giveId())
           id = input()
           data.dataUnvis = data.deleteMarker(data.dataUnvis, id, True)
           ifSaveUnvis = True
       elif choice != "6":
           print(Messages.noOptInMenu())
       if choice == "6":
           print(Messages.ifSaveFiles())
           quitMenu = input()
           if quitMenu.lower() != "yes" and quitMenu.lower() != "no":
               choice = 0
           elif quitMenu.lower() == "no":
               exit(0)    
           elif quitMenu.lower() == "yes":
               print(Messages.saving())
               if ifSaveVis:
                   data.dataVis.to_csv("visited.txt", index = False, encoding = "utf-8")
               if ifSaveUnvis:
                   data.dataUnvis.to_csv("to_visit.txt", index = False, encoding = "utf-8")
               if ifSaveVis or ifSaveUnvis:
                   web_map.main()   
               input()
               exit(0)                           
           input()            
           clear()

if __name__ == "__main__":
    main()