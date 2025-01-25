brands = ["gucci", "guess", "versace", "lacoste", "armani"]
newlist = []
for x in brands:
    if "a" in x:
        newlist.append(x)
print(newlist)
newlist = [x for x in range(10) if x < 5]

print(newlist)
