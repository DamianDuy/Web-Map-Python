import pandas
from os import system, name

dataVis = pandas.read_csv("visited.txt")
dataUnvis = pandas.read_csv("to_visit.txt")

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

def addMarkerVis(dataVisual):
    name = input("Give the name of the place: ")
    country = input("Give the name of the country: ")
    rateTem = input("Rate the place out of 10: ")
    latitude = input("Give the latitude: ")
    longitude = input("Give the longitude: ")
    if ifFloat(latitude) and ifFloat(longitude):
        latitude = float(latitude)
        longitude = float(longitude)
    else:
        print("Coordinates must be numbers.")
        return dataVisual        
    while not ifFloat(rateTem) or float(rateTem) not in range (0,11):
        print("Rate must be a number between 0 and 10.")
        rateTem = input("Rate the place out of 10: ")  
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

def addMarkerUnvis(dataVisual):
    name = input("Give the name of the place: ")
    country = input("Give the name of the country: ")
    latitude = input("Give the latitude: ")
    longitude = input("Give the longitude: ")
    if ifFloat(latitude) and ifFloat(longitude):
        latitude = float(latitude)
        longitude = float(longitude)
    else:
        print("Coordinates must be numbers.")
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

def deleteMarker(dataVisual, id, ifShowMessage):
    ifExists = False
    if ifFloat(id):
        id = float(id)
    elif ifShowMessage:
        print("ID must be a number.")
        return dataVisual    
    for i in list(dataVisual["ID"]):
        if id == i:
            dataVisual.drop(dataVisual[dataVisual.ID == i].index, inplace = True)
            ifExists = True
    if not ifExists and ifShowMessage:
        print("Position with the given ID does not exist.")
    return dataVisual

def changeMarker(dataVisualVis, dataVisualUnvis, id):
    ifExists = False
    if ifFloat(id):
        id = float(id)
    else:
        print("ID must be a number.")
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
        print("Position with the given ID does not exist.")
        return dataVisualVis
    rateTem = input("Rate the place out of 10: ")    
    while not ifFloat(rateTem) or float(rateTem) not in range (0,11):
        print("Rate must be a number between 0 and 10.")
        rateTem = input("Rate the place out of 10: ")  
    newRate = rateTem + "/10"    
    dfTem = pandas.DataFrame({"ID" : [num],
                              "NAME": [newName],
                              "COUNTRY": [newCountry],
                              "RATE": [newRate],
                              "LAT": [newLatitude],
                              "LON": [newLongitude]})
    return dataVisualVis.append(dfTem, ignore_index = True)    

def showMenu():
    print("1. Add marker to visited.")
    print("2. Add marker to unvisited.")
    print("3. Change marker to visited.")
    print("4. Delete marker from visited.")
    print("5. Delete marker from unvisited.")
    print("6. Exit")

ifSaveVis = False
ifSaveUnvis = False
choice = "0"
while choice != "6":
    showMenu()
    choice = input()
    clear()
    if choice == "1":
        dataVis = addMarkerVis(dataVis)
        ifSaveVis = True
    elif choice == "2":
        dataUnvis = addMarkerUnvis(dataUnvis)
        ifSaveUnvis = True
    elif choice == "3":
        id = input("Give ID of the place: ")
        dataVis = changeMarker(dataVis, dataUnvis, id)
        dataUnvis = deleteMarker(dataUnvis, id, False)
        ifSaveVis = True
        ifSaveUnvis = True
    elif choice == "4":
        id = input("Give the ID of the place: ")
        dataVis = deleteMarker(dataVis, id, True)
        ifSaveVis = True
    elif choice == "5":
        id = input("Give the ID of the place: ")
        dataUnvis = deleteMarker(dataUnvis, id, True)
        ifSaveUnvis = True
    elif choice != "6":
        print("No such option in the menu.")
    if choice == "6":
        quitMenu = input("Do you wish to save? Type yes/no: ")
        if quitMenu.lower() != "yes" and quitMenu.lower() != "no":
            choice = 0
        elif quitMenu.lower() == "yes":
            print("Saving...")
            if ifSaveVis:
                dataVis.to_csv("visited.txt", index = False, encoding = "utf-8")
            if ifSaveUnvis:
                dataUnvis.to_csv("to_visit.txt", index = False, encoding = "utf-8")
            input()                         
    if choice != "6":    
        input()            
        clear()