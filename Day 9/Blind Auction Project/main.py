# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
from os import system
user_dictionary = {}
flag =1
#Input from user
while flag ==1:
    print(art.logo)
    name = input("Enter your name: ")
    bid = input("Enter your bid amount: Rs")
    user_dictionary[name] = bid
    bid_status = input("Is there any one else who wanna bid type 'yes' or 'no' : ").lower()
    if bid_status == 'yes':
        flag =1
    else:
        flag =0
    # print("\n"*20)
    system("clear")
# checking inside the dictionary
final_key =""
highest_bid_value = 0
highest_bidder=""
for key in user_dictionary:
    bid_value = int(user_dictionary[key])
    if bid_value >= highest_bid_value:
        highest_bid_value = bid_value
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of Rs{highest_bid_value}")
# print(highest_bidder )
# print( highest_bid_value)
# print(user_dictionary)