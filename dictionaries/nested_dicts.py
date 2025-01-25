cosmetics = {
    "Foundation": {
        "name": "Dior",
        "shade": "21N"
    },
    "Blush": {
        "name": "SHU",
        "shade": "623"
    },
    "Lipstick": {
        "name": "Max Factor",
        "shade": "828"
    }
}
print(cosmetics)
print(cosmetics["Foundation"]["name"])
for x, y in cosmetics.items():
    print(x)

    for z in y:
        print(z + ':', y[z])