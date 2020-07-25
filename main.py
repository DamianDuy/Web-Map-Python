import pandas
from os import system, name

dataVis = pandas.read_csv("visited.txt")
dataUnvis = pandas.read_csv("to_visit.txt")

def clear():
    if name == "posix":
        _ = system("clear")
    else:
        _ = system("cls") 

def addMarkerVis(dataVisual):
    idVis = list(dataVisual["ID"])
    if not idVis:
        i = 1
    else:
        i = idVis[-1] + 1
    name = input("Give the name of the place: ")
    country = input("Give the name of the country: ")
    rateTem = input("Rate the place out of 10: ")
    latitude = float(input("Give the latitude: "))
    longitude = float(input("Give the longitude: "))
    rate = rateTem + "/10"
    dfTem = pandas.DataFrame({"ID" : [i],
                              "NAME": [name],
                              "COUNTRY": [country],
                              "RATE": [rate],
                              "LAT": [latitude],
                              "LON": [longitude]})
    dataVisual = dataVisual.append(dfTem, ignore_index = True)
    return dataVisual

def addMarkerUnvis(dataVisual):
    idUnVis = list(dataVisual["ID"])
    if not idUnVis:
        i = 1
    else:
        i = idUnVis[-1] + 1
    name = input("Give the name of the place: ")
    country = input("Give the name of the country: ")
    latitude = float(input("Give the latitude: "))
    longitude = float(input("Give the longitude: "))
    dfTem = pandas.DataFrame({"ID" : [i],
                              "NAME": [name],
                              "COUNTRY": [country],
                              "LAT": [latitude],
                              "LON": [longitude]})
    dataVisual = dataVisual.append(dfTem, ignore_index = True)
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
        
    elif choice == "2":
        dataUnvis = addMarkerUnvis(dataUnvis)
    elif choice == "3":
        print("Changing")
    elif choice == "4":
        print("Deleting")
    elif choice == "5":
        print("Deleting")
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