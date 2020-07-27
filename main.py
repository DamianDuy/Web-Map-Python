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
    if ifFloat(rateTem):
        rateTem = float(rateTem)
    else:
        print("Rate must be number.")
        return dataVisual
    if rateTem not in range (0,11):
        print("Rate must be between 0 and 10.")
        return dataVisual
    rateTem = str(rateTem)
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

def deleteMarker(dataVisual):
    ifExists = False
    id = input("Give the ID of the place: ")
    if ifFloat(id):
        id = float(id)
    else:
        print("ID must be a number.")
        return dataVisual    
    for i in list(dataVisual["ID"]):
        if id == i:
            dataVisual.drop(dataVisual[dataVisual.ID == i].index, inplace = True)
            ifExists = True
    if not ifExists:
        print("Position with the given ID does not exist.")
    return dataVisual

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
        print("Changing")
        ifSaveVis = True
        ifSaveUnvis = True
    elif choice == "4":
        dataVis = deleteMarker(dataVis)
        ifSaveVis = True
    elif choice == "5":
        dataUnvis = deleteMarker(dataUnvis)
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