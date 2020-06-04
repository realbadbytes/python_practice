nums = [88, 72, 23, 15, 17, 19, 90]

for n in nums:
    if n%2 == 0
        do_something(n)

# separate the picking and the doing

def evens(stream):
    them = []
    for n in stream:
        if n%s == 0:
            them.append(x)
    return them

for n in evens(num):
    do_something(n)

# separations has been accomplished
# function takes the stream, iterator is used
# however, this is not the best way
# instead, use a generator
# generator is like a function. produces an iterator
# when you get a value from the iterator, it yields values

def hello_world():
    yield "Hello"
    yield "World"

for x in hello_world():
    print(x)

#Hello
#World
# the generator gives values as they ready. "Yield to the oncoming value, let it go"

def evens(stream):
    for n in stream:
        if n%2 == 0:
            yield n

for n in evens(nums):
    do_something(n)

# this removes the need for return values and the temp lists
# gives values as soon as they are ready
# it does not care how long the stream is, the generator produces values as they are encountered

# range of huge ass number will run out of space, xrange of huge ass number will run out of time

