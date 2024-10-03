# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates
#   Set = {} unordered and immutable, but Add/Remove OK. NO Duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. Faster

#########################################################################################
# LISTS:

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits)) 
# print(help(fruits)) #Gives help 
# print(len(fruits)) #
# print("pineapple" is fruits) # Tells if it is in the list (True or False)

# fruits[0] = "pineapple" # Can REASSIGN values in list
# fruits.append("pineapple") # Adds to list
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))

#print(fruits)
##########################
# for fruit in fruits:
  #  print(fruits)

#cars = ["bmw","maserati","audi","mercedes","ferrari"]
#print(f"These are list of {cars}")
#print(f"The first car is {cars[0]}")

#print(f"The last car is {cars[-1]}")
#cars[-1] = "Lamborghini"
#print(f"The last car is {cars[-1]}")

# adding a new value to the list
#cars.append("bugatti")
#print(cars)

# removing a value from the list
#cars.remove("maserati")
#print(cars)

# looping through the list
#otherwise called iterating through the list
#for car in cars:
   # print(len(car))
   # print(car)
   # carRequest = input ("add a new car please: ")
   # cars.append(carRequest)
   # print(cars)
   # print(len(cars))
   # print(cars.upper())
   # print(cars)
   # if len(cars) > 10:
       # break

############ CHALLENGE ###################

# create a list of friends
# make sure the initial list is none
#friends = []
# add a new friend to the list, add at least 5 friends
#friends = ["Yahir","Vinny","Isabella","Enrique","Jaden"]
# remove a friend
#friends.remove("Jaden")
# insert a friend at a specific index, maybe 2
#friends.insert(2, "Ohtani")
# print the list of friends
#print(friends)
# loop through the list and print the friends names
# see if a particular friend is in the list (boolean value)
# if the list is greater than 10, break the loop.
#for friends in friends:
    #print(len(friends))
    #print(friends)
    #if len(friends) > 10:
        #break

#print("Jaden" is friends)

#########################################################################################
# SETS:

# fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(lens(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple") # Adds to the set
# fruits.remove("apple") # Removes from the set
# fruits.pop() # Randomly takes one
# fruits.clear()

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)
# for fruit in fruits:
    #print(fruit)

#########################################################################################
# DICTIONARY -----> A collection of {key:value} pairs
#                   ordered and changeable. No duplicates


capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}


# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("India"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist.")  # Checks if "capital" is apart of set

# capitals.update({"Germany": "Berlin"}) # Adds Germany into the set
# capitals.update({"USA": "Detroit"}) # Changes "USA" Capital from "WASHINGTON D.C." to "DETROIT"
# capitals.pop("China") # Pop, pops out whatever you want
# capitals.popitem()    # Pops out a random item
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#    print(value)


# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")