#Creates three different sets with the same three elements
letter_set = set(['a', 'b', 'c'])
string_set = set ('abc')
another_string_set = set('aabbbccc')

new_set = set (['abc']) #Set with just one element of abc

word_set = set (['one', 'two', 'three'])
print (word_set)

print ()

#set_variable.add (element) #Add element into a set
#set_variable.update (element_list) #Add a bunch of elements into a set

letter_set.add ('def') #Add one element of "def", does not pull them apart
print (letter_set)

print ()

set1 = set([12, 24, 36])
set2 = set(['one', 'two', 'three'])
set1.update(set2) #Adds the three elements from set2 into set 1
print(set1)
print()

#set_variable.remove (element) #Removes an element, but causes an error if element doesn't exist
#set_variable.discard (element) #Removes an element, does not cauase an error if element isn't there

letter_set = set(['a', 'b', 'c'])
letter_set.remove('c') #Removes c from the set
print(letter_set)

print()

set1 = set([12, 24, 36])
set1.discard(12) #Gets rid of the 12 element in the set
#set1.remove(12) #Causes an error message since 12 is not in the set
print(set1)
print()

name_set = set(['Clint', 'Katie', 'Caryn'])
for name in name_set: #For every element in the set
    print(name) #Prints each name in the set on a separate line
print()

#set1_variable.union(set2_variable) #Gets all unique elements from both of the sets, not duplicates
#set1_variable | set2_variable #Alternative method

set1 = set(['a', 'b', 'c'])
set2 = set(['c', 'd', 'e'])
set3 = set1.union(set2) #Combines both sets into a new set with 5 different elements
print(set3)
print()

#set1_variable.intersection(set2_variable) #Finds the elements that are shared in both sets
#set1_variable & set2_variable #Alternative method

set1 = set(['a', 'b', 'c'])
set2 = set(['c', 'd', 'e'])
set3 = set1.intersection(set2) #Creates a new set with only the c element
print(set3)
print ()

#set1_variable.difference(set2_variable) #Finds the unique elements in the first set
#set1_variable - set2_variable #Alternative method
set1 = set(['a', 'b', 'c'])
set2 = set(['c', 'd', 'e'])
set3 = set1.difference(set2) #Creates a new set with only a and b elements, unique to set 1
set4 = set2.difference(set1) #Creates a new set with only d and e elements, unique to set 2

#set1_variable.symmetric_difference(set2_variable) #Unique elements of both set, ignore overlaps
#set1_variable ^ set2_variable #Alternative method

set1 = set(['a', 'b', 'c'])
set2 = set(['c', 'd', 'e'])
set3 = set1.symmetric_difference(set2) #Creates a new set with 4 unique elements, ignoring c
print(set3)
