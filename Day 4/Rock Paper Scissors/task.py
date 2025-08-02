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
user_choice = input("What do you choose? type 0 for rock, 1 for paper, 2 for scissors \n")
computer_choice = random.randint(0,2)
computer_choice = str(computer_choice)
if user_choice == "0":
    print(rock)
elif user_choice =="1":
    print(paper)
else:
    print(scissors)
# computer choice
print("Computer Chose: ")
if computer_choice == "0":
    print(rock)
elif computer_choice =="1":
    print(paper)
else:
    print(scissors)

# winner decision
if computer_choice == user_choice:
    print("It's a draw")
elif computer_choice == "0" and user_choice == "1":
    print("You Win!")
elif computer_choice == "1" and user_choice == "2":
    print("You Win!")
elif computer_choice == "2" and user_choice == "0":
    print("You Win!")
    print(r''' 
       /(|
      (  :
     __\  \  _____
   (____)  `|
  (____)|   |
   (____).__|
    (___)__.|_____''')

else:
    print("You loose")
    print(r'''
          .-.                     .-.
          |U|                     | |
          | |                     | |
          | |                     | |
         _| |_                   _| |_
        | | | |-.               | |_| |-.
       /|     ` |              / )| |_|_|
      | |       |             | |-' `-^-'
      |         |             |     ||  |
      \         /             \     '   /
       |       |               |       |
       |       |               |       |
                                            ''')