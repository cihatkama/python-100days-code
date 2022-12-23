print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

variable_name1 = name1.lower()
variable_name2 = name2.lower()

#Counting for each letter [name1]
T = variable_name1.count("t")
R = variable_name1.count("r")
U = variable_name1.count("u")
E = variable_name1.count("e")

L = variable_name1.count("l")
O = variable_name1.count("o")
V = variable_name1.count("v")
E = variable_name1.count("e")

#Counting for each letter [name2]
T2 = variable_name2.count("t")
R2 = variable_name2.count("r")
U2 = variable_name2.count("u")
E2 = variable_name2.count("e")

L2 = variable_name2.count("l")
O2 = variable_name2.count("o")
V2 = variable_name2.count("v")
E2 = variable_name2.count("e")

#total points
total_points_FirstDigit = (T + R + U + E) + (T2 + R2 + U2 + E2) 

total_points_SecondDigit = (L + O + V + E) + (L2 + O2 + V2 + E2)

Two_Digit_Number = int(str(total_points_FirstDigit) + str(total_points_SecondDigit))

#printed results function
def printed_results():
    if Two_Digit_Number < 10 or Two_Digit_Number > 90:
      print(f"Your score is {Two_Digit_Number}, you go together like coke and mentos.")
    elif 40 < Two_Digit_Number < 50:
      print(f"Your score is {Two_Digit_Number}, you are alright together.")
    else:
      print(f"Your score is {Two_Digit_Number}.")

#Condition and the function calling
if variable_name1 == "true love" or variable_name2 == "true love":
    print("""Wait, try something different from "True Love!" """)

else:
    printed_results()