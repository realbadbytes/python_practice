#!/usr/bin/python3

# tuple - ummutable
# if the data should never change, use a tuple

# list
vowels = [ 'a', 'e', 'i', 'o', 'u' ]
print (type(vowels))
# tuple
vowels2 = ( 'a', 'e', 'i', 'o', 'u' )
print (type(vowels2))
# immutable!
# vowels2[2] = 'I'
# print (vowels2)

# single object tuples are scary. To be a tuple, needs to have comma
t = ('Chris')
print (type(t))
t2 = ('Chris',)
print (type(t2))
