
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(options[user_option])

pc_option = random.randint(0, 2)
print("Computer chose:")
print(options[pc_option])

if user_option >= 3 or user_option < 0: 
  print("You typed an invalid number, you lose!") 
elif user_option == 0 and pc_option == 2:
  print("You win!")
elif pc_option == 0 and user_option == 2:
  print("You lose")
elif pc_option > user_option:
  print("You lose")
elif user_option > pc_option:
  print("You win!")
elif pc_option == user_option:
  print("It's a draw")