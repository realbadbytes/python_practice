names = ["Eiffel Tower", "Empire State", "Sears Tower"]
heights = [324, 381, 442]

for i in range(len(names)):
    name = names[i]
    height = heights[i]
    print("%s: %s meters" % (name, height))

# no. use zip, create pairs
# zip takes an iterable, creates a new iterable
for name, height in zip(names, heights):
    print("%s: %s meters" % (name, height))

# dict() accepts stream of pairs
pairs_stream = dict(zip(names, heights))
print(pairs_stream)

tall_buildings = {
    "Empire State": 381,
    "Sears Tower": 442,
    "Burj Khalifa": 828,
    "Taipei 101": 509,
    }

# manipulate with max function, get the tuple instead of just value
# docs: when one posn arg is provided, it must be an iterable
# key argument specifies one-argument ordering function, like list.sort()
# lambda arguments: expression
# the key lamdba here takes the tuple result of max of items(), then gets the second index
print(max(tall_buildings.items(), key=lambda b: b[1]))

print(max(tall_buildings, key=tall_buildings.get))


