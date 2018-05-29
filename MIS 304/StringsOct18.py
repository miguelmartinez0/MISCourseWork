name = "Mickey Mouse"

char1 = name[0] #Grabs the first character in the string

char2 = name[7] #Grabs the eigth character in the string

print (char1, char2) #Prints the first and eight character

print (len(name)) #Prints how many characters in the string

print()

name = 'John Jacob Jingleheimer Schmidt'

first = name[:4] #Grabs the first four characters

second = name[5:10] #Grabs characters 6-11

third = name[11:23] #Grabs characters 12-24

last = name[24:] #Grabs all the characters after the 24th one

print (last, ',', first)

print()

name_list = name.split() #Divides string at each space by default

print (name_list) #Prints the list of four different names

print()

address = '123 Main St*Austin*TX*78705'

address_list = address.split('*') #Divides string at each asterisk

for item in address_list: #Create a loop to print each different piece of the address

    print(item) #Print each item on a separate line

print()

###

phonebook_dict = {'Clint':'505-2612', 'Katie':'505-3451'} #2 elements, Names as key, Numbers as value

print(phonebook_dict)

quiz_dict = {'jwt254':[83, 92, 89], 'fkw928':[85, 94, 96]} #2 elements, Eids as key, Lists of grades as value

print(quiz_dict)

test_dict = {} #Create an empty dictionary

print(phonebook_dict['Katie']) #Print just Katie's values from the dictionary, similar to lists and index

print()

for key in phonebook_dict: #Loop to print all data from a dictionary

    print(key) #Prints the keys from the key value pairs on a separate line

print()

for key in phonebook_dict: #Loop to print all data from a dictionary

    print(key, phonebook_dict[key]) #Prints the keys and values from the key value pairs on a separate line

print ()

phone_dict = {'Clint':'505-2612', 'Katie':'505-3451'} #Create a new dictionary

phone_dict['Caryn'] = '505-2612' #Add the new key value pair to the dictionary

print(phone_dict) #Print the dictionary with the new added value

print(len(phone_dict)) #Print how many key value pairs there are









