# loop like a native talk
# youtube.com/watch?v=EnSu9hHGq5o
# circa 2013

# not pythonic
i = 0
while i < len(my_list):
    v = my_list[i]
    print(v)
    i += 1

# pythonic but rube goldbergy
for i in range(len(my_list)):
    v = my_list[i]
    print(v)

# more pythonic, iterate directly on the elements, dont use ints
for v in my_list:
    print(v)

# iterable produces stream of values
# assigns each stream value to the name
# iterable decides what values it produces
# lots of things are iterables
for name in iterable:
    statements

# iterate list, get elements
# iterate string, get chars
# iterate dict, get keys (not values)
# iterate file, get lines
for k in d:
    print k
# can use itervalues() or iteritems() as well
# os.walk produces an iterable too! root, dirs, files each time
# itertools has crazy iterators, see chain, repeat, cycle

# how do i get the index?
# not using the fucking index number, not pythonic
# get the index via enumerate() which gives index and original value
names = ["tower", "state", "headphones"]
list(enumerate(names))
# returns list of tuples, (index, value)
# this removes focus from the index number within the code, more readable and pythonic

# absolutely awful
# the i is basically a sidecar motorcycle
i = 0
for v in iterable:
    print(i, v)
    i += 1























