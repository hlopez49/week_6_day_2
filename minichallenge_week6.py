#######################################Dictionaries###############################
# Dictionaries Practice #1
# Create a dictionary called fruits with the following key-value pairs:
fruits_colors = {"apple":"red", "banana":"yellow", "mango":"green", "cherry":"red", "watermelon":"green"}
# apple --> red
# banana --> yellow
# mango --> green
# cherry --> red
# watermelon --> green
# Display the dictionary on the screen.
print(fruits_colors)

# Dictionaries Practice #1
# Create a dictionary called my_dict that stores the following information about a person:
# name: Karen
# surname: Jurgens
# age: 35
# occupation: Journalist
# The names of the keys and values must be equal to the ones indicated above.
my_dict = {"Name": "Karen", "Surname": "Jurgens", "Age": "35", "Occupation": "Jounrnalist"}
# print(my_dict)

# for key in my_dict:
#     print(f"these are the {key}")

# # print the values in the dictiobary
# for value in my_dict.values():
#     print(value)    

# my_dict_all= my_dict.items() #key value pairs
# for key, value in my_dict_all:
#     print(f"{key} is the description of {value}")

# #   Dictionaries Practice #2
# # Use print to returns the second item of the list called points2, inside the following dictionary.
# # If the value 300 were to change in the future, the code should work the same to return the value at that same position. To do this, you must refer to the names of the keys and/or indexes as appropriate.
# my_dictio = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
# print(my_dictio["points"]["points2"][1]) #Use dictionary indices to extract the second item of points2


# Dictionaries Practice #3
# Update the information in our dictionary called my_dict (reassigning new values to the keys as appropriate), and add a new key called "country" (without a tilde). The new data is:
# name: Karen
# surname: Jurgens
# age: 36
# occupation: Editor
# country: Colombia
# to do this, you should not change the line of code already written, but update the values using dictionary methods.
#my_dict = {"name":"Karen", "surname":"Jurgens", "age":35, "occupation":"Journalist"}
my_dict.update({"Country": "Columbia"})
print(my_dict)
my_dict["Occupation"] = "Editor"
print(my_dict)


################################Tuples##################################


# Tuples Practice #1
#tuples are immutable and are defined using parentheses
# Create a tuple called my_tuple with the following values:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# do it
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Display the tuple on the screen.
print(my_tuple)
# when are they useful? You can do index on tuples while you cant do it on lists
# Tuples are useful when you want to store a collection of items that should not be changed, such as days of the week, months of the year, etc.






# Use a tuple method to count the number of times the value 2 appears in the following tuple, and display the result (integer) on the screen:


# my_tuple = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)


# Tuples Practice #2
# Convert the following tuple to a list, and store it in a variable called my_list.


# my_tuple = (1, 2, 3, 2, 3, 1, 3, 2)


# Tuples Practice #3
# Extract the elements of the following tuple into four variables: a, b, c, d


# my_tuple = (1, 2, 3, 4)


###############################SETS########################################
# Sets Practice #1
# Join the following sets into one, called my_set_3:
# {1, 2, "three", "four"}
# {"three", 4, 5}
# my_set_1 = {1, 2, "three", "four"}


# my_set_2 = {"three", 4, 5}


# Sets Practice #2
# Remove a random item from the following set, using set methods.
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}


# Sets Practice #3
# Add the name Gunther to the following set, using set methods:
# raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}


###########################Booleans#######################################


# Booleans Practice #1
# Make a comparison that returns a boolean and store the result (True/False) in a variable called test


# Booleans Practice #2
# Check if 17834/34 is greater than 87*56 and print the boolean result to the screen using print()


# Booleans Practice #3
# Check if the square root of 25 is equal to 5 and display the result (boolean) on the screen using print()


###############################Proceed to last slide#################################
