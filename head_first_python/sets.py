#!/usr/bin/python3

# set - data structure where duplicate vales are forbidden and maintains insertion order

vowels = { 'a', 'a', 'e', 'e', 'i', 'o', 'o', 'o', 'u' }
print ("set of vowels {}".format(vowels))

# can also create a set with set() 

vowels2 = set('aaaeeeiiiooouuu')
print ("vowels2 {}".format(vowels2))

word = "hello"
print (vowels2.union(word))
print (vowels2.intersection(word))
print (vowels2.difference(word))




