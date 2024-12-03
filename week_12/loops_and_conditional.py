
# import math
# total = []
# prices = input("Enter price of item(s) (Enter 'checkout' to Quit): ")


# while prices != "checkout":
#     total.append(prices)
#     prices = input("Enter price of item(s) (Enter 'checkout' to Quit): ")

# total_price = sum(total)

# if total_price < 200:
#     print(f"You're NOT ELIGIBLE for a discount. You're total price is {total_price}")

# elif total_price > 200 and total_price < 500:
#     total_price*0.85
#     print(f"You're ELIGIBLE for a 15% discount. You're total price is {total_price}")

# elif total_price > 500:
#     total_price*0.80
#     print(f"You're ELIGIBLE for a 20% discount. You're total price is {total_price}")



########### FIXED VERSION: ########



total = []  # Initialize an empty list to store prices

# Continuously ask for item prices until the user types "checkout"
while True:
    prices = input("Enter price of item(s) (Enter 'checkout' to quit): ")
   
    if prices.lower() == 'checkout':
        break  # Exit the loop if the user types 'checkout'
   
    if prices.replace('.', '', 1).isdigit():  # Check for valid numeric input
        total.append(float(prices))  # Convert to float and append to total
    else:
        print("Invalid input. Please enter a valid price or type 'checkout'.")

# Calculate the total price of the items
total_price = sum(total)

# Apply discounts based on the total price
if total_price < 200:
    print(f"You're NOT ELIGIBLE for a discount. Your total price is ${total_price:.2f}")
elif 200 <= total_price < 500:
    total_price *= 0.85  # Apply a 15% discount
    print(f"You're ELIGIBLE for a 15% discount. Your total price is ${total_price:.2f}")
elif total_price >= 500:
    total_price *= 0.80  # Apply a 20% discount
    print(f"You're ELIGIBLE for a 20% discount. Your total price is ${total_price:.2f}")
