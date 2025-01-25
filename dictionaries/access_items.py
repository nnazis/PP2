thisdict = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 1980
}
print(thisdict)
x = thisdict["model"] #or thisdict.get("model")
print(x)
x = thisdict.keys() #showing only keys
print(x)
thisdict["color"] = "black" #add new item
print(x)
x = thisdict.values() #showing only values
print(x)
x = thisdict.items() #showing all items
print(x)