# Problem 1: Student Grade Categorization
# Ask the user to enter a list of student scores (one by one).
# Use a while loop to continuously accept scores until the user enters a negative number.
# For each score, use nested if statements to categorize the score:
# 90-100: Print "Excellent"
# 70-89: Print "Good"
# 50-69: Print "Pass"
# Below 50: Print "Fail"
# Stop the loop and print the final count of each category when the user enters a negative number.

scores = [] # Creates score as a list
numbers = int(input("Enter a student's score (enter negative to quit): ")) # Asks for list of student scores


while numbers >= 0:
    scores.append(numbers)
    numbers = int(input("Enter a student's score (enter negative to quit): ")) # Continues a loop asking for a score until a negative number is entered

print(scores)


if scores[0] in range(90, 101): # Checks for scores between 90-100
     print("Excellent")
elif scores[0] in range(70, 90): # Checks for scores between 70-90
     print("Good")
elif scores[0] in range(50, 70): # Checks for scores between 50-70
     print("Pass")
elif scores[0] in range (1, 50): # Checks for scores below 50
     print("Fail")

if scores[1] in range(90, 101): # Checks for scores between 90-100
     print("Excellent")
elif scores[1] in range(70, 90): # Checks for scores between 70-90
     print("Good")
elif scores[1] in range(50, 70): # Checks for scores between 50-70
     print("Pass")
elif scores[1] in range (1, 50): # Checks for scores below 50
     print("Fail")

if scores[2] in range(90, 101): # Checks for scores between 90-100
     print("Excellent")
elif scores[2] in range(70, 90): # Checks for scores between 70-90
     print("Good")
elif scores[2] in range(50, 70): # Checks for scores between 50-70
     print("Pass")
elif scores[2] in range (1, 50): # Checks for scores below 50
     print("Fail")


if scores[3] in range(90, 101): # Checks for scores between 90-100
     print("Excellent")
elif scores[3] in range(70, 90): # Checks for scores between 70-90
     print("Good")
elif scores[3] in range(50, 70): # Checks for scores between 50-70
     print("Pass")
elif scores[3] in range (1, 50): # Checks for scores below 50
     print("Fail")

if scores[4] in range(90, 101): # Checks for scores between 90-100
     print("Excellent")
elif scores[4] in range(70, 90): # Checks for scores between 70-90
     print("Good")
elif scores[4] in range(50, 70): # Checks for scores between 50-70
     print("Pass")
elif scores[4] in range (1, 50): # Checks for scores below 50
     print("Fail")




# if scores in range(70, 90): # Checks for scores between 70-89
#      print("Good")

# if scores in range(50, 70): # Checks for scores between 50-69
#      print("Pass")

# if scores in range(1, 50): # Checks for scores below 50
#      print("Fail")



# while scores 
# if scores[0] in range(90, 100):
#      print("Excellent")
# elif scores in range(70, 89):
#      print("Good")
# elif scores in range(50,69):
#      print("Pass")
 



# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

########################################################################################

# food = input("Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")

# print("bye")










# Problem 2: Even and Odd Counter with Conditions
# Ask the user for a starting and ending number.
# Use a for loop to iterate from the starting to the ending number.
# Inside the loop:
# Use nested if to check if the number is both even and greater than 10. If true, count it as a “special even” number.
# If it’s odd and less than 20, count it as a “special odd” number.
# Print the counts for both “special even” and “special odd” numbers.

# Starting_number = int(input("Enter a starting Number: "))     # Asks user for a Starting Number
# ending_number = int(input("Enter a ending number: "))     # Asks user for a Ending Number 

# for num in range(Starting_number, ending_number):


# if num >10:       # Checks if the numbers between the Starting and Ending numbers are greater than 10 
#     if num %2 == 0:       # If the last one is true, checks if the numbers are even
#         print("Number is a special even number ")     #If both statements are true, prints "Number is a special even number"
# elif num%2 != 0:      # If the other statements werent true, checks if the number is odd
#     if num < 20:      # If true, checks if the number is less than 20
#         print("Number is a special odd number")       # If both are true, prints "Number is a special odd number"












# if Starting_number >10:
#     if Starting_number%2 == 0:
#         print("Starting number is a special even number ")
# elif Starting_number%2 != 0:
#     if Starting_number < 20:


# if ending_number >10:
#     if ending_number%2 == 0:
#         print("Ending number is a special even number ")
