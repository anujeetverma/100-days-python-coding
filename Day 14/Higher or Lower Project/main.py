#TODO import the important modules
import random
from game_data import data
import art

#TODO make a random function name "selector" items from the data list and name them A and B

def selector():
    choice = random.randint(0,len(data)-1)
    return choice


#TODO make a variable named "point" to keep a track of points
#TODO write the function to select two random options
A,B={},{}
score = 0
def team_selector():
    global A,B
    print(art.logo)
    A = data[selector()]
    print(f"compare A: {A['name']}, {A['description']}, from {A['country']}")
    # print(A)

    print(art.vs)

    B = data[selector()]
    print(f"compare B: {B['name']}, {B['description']}, from {B['country']}")
    # print(B)

#TODO write a function named "verifier" that takes checks the result and compare the option
# and tells whether its correct or not

def verifier():
    global A,B,user_input
    if A['follower_count'] >= B['follower_count']:
        return 0
    elif A['follower_count'] <= B['follower_count']:
        return 1
    print(f"your score is: {score}")

flag =1
while flag ==1:
    team_selector()
    #TODO take user input of their choice

    try:
        user_input = input("Who has more followers? Type 'A' or 'B':  ").strip().lower()
        if user_input not in ('a', 'b'):
            user_input = input("Invalid input. Type 'A' or 'B': ").strip().lower()
        if user_input == 'a':
            user_input = 0
        elif user_input == 'b':
            user_input = 1
        else:
            if ValueError:
             user_input = input("Type 'A' or 'B':  ").lower()
    except Exception as e:
        print("Error:", e)



    if user_input !=verifier():
        print("not-correct")
        print(f"your score is: {score}")
        flag =0
    else:
        print("\n"*20)

        print("correct")
        score += 1
        print(f"your score is: {score}")
        A = B
        B = data[selector()]












