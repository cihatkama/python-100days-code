# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_for_small_pizza = 2
pepperoni_for_medium_or_large_pizza = 3
extra_cheese_for_any_size_of_pizza = 1

# for pizza size
if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
else:
    total_bill += 25

# for pepperoni selection
if add_pepperoni == "Y":
    if size == "S":
        total_bill += 2
    else:
        total_bill += 3

# for extra cheese selection
if extra_cheese == "Y":
    total_bill += 1

print(f"Your final bill is ${total_bill}.")