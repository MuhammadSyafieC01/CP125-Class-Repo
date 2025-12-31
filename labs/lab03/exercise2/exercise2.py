def find_station(stations, name):
    if name in stations:
        index = 0
        for i in stations:
            if name == i:
                print(i)
                print(index)
                break
            index +=1

def count_stops(stations, start, stop):
    pass

stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]

find_station(stations,"Orchard")