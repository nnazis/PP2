thisset = {"Almaty", "Atyrau", "Aqtobe", "Shymkent"}
thisset.add("Kostanay")
print(thisset)

set2 = {"Moskow", "Saint-Peterburg", "Orenburg"}
thisset.update(set2)
print(thisset)
#can add any iterable object
mytuple = ("Seoul", "Busan")
thisset.update(mytuple)
print(thisset)