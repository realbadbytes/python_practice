#!/usr/bin/python3

# remove - remove value from list, shrinking list or raising error
nums = [ 1, 2, 3, 4 ]
print (nums)
nums.remove(3)
print (nums)

# pop - remove at index, or pop last element
popped = nums.pop()
popped2 = nums.pop(1)
print (popped)
print (popped2)

# extend - take list of objects, add to other list
nums.extend([5, 6])
print (nums)

# insert - insert at index in list (index, object)
nums.insert(0, 1)
print (nums)
nums.insert(2, 'two-and-a-half')
print (nums)

# copying lists
first = [1, 2, 3, 4]
second = first
print (first)
print (second)
second.append(7)
print (first)
# perform deep copy
third = second.copy()
second.append(9)
print (third)

# start, stop , step
# slicing does not alter the original list
nums = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print (nums)
# start at index 0, step 4, stop at 10 [start: stop: step]
print (nums[0:10:4]) 
# start at index 2, step 2, stop at end (-1 index)\
print (nums[2:-1:2]) 
# all nums except at index 10
print (nums[:10])

# turn string into list
string_test = "This is a string dude"
letters = list(string_test)
print (letters)
print (letters[0:3])
print (''.join(letters[0:3]))
# select last 6 objects
print (''.join(letters[-6:]))

# reverse string
backwards = letters[::-1] # start 0, step 0, stop at -1
# index -1, index -2, index -3, etc until what?
print (''.join(backwards))

# every other in reversed
print (''.join(letters[::2]))

# iterating
tab_counter = 1
for char in letters:
    if char == ' ':
        tab_counter += 1
    print ('\t'*tab_counter, char)







