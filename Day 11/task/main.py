import random
import art
print(art.logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_cards = []
player_cards = []
dealer_cards.append(cards[random.randint(0,12)])
dealer_cards.append(cards[random.randint(0,12)])
player_cards.append(cards[random.randint(0,12)])
player_cards.append(cards[random.randint(0,12)])
print(dealer_cards)
print(f"dealer card {dealer_cards}the sum of = {sum(dealer_cards)}")
print(f"player cards {player_cards}the sum = {sum(player_cards)}")

# choice = input("Do you want to withdraw another card 'y' or type 'n'").lower()
# while choice == 'y':
#     player_cards.append(cards[random.randint(0, 12)])
#     if sum(player_cards) > 21:
#         print("You loose")
#         print("Dealer Win")
#         print(f"the sum of player card = {sum(player_cards)}")
#         choice = "n"
#     else:
#         print(f"the sum of player card = {sum(player_cards)}")
#         choice = input("Do you want to withdraw another card 'y' or type 'n'").lower()
# print(f"the sum of player card = {sum(player_cards)}")
# if sum(player_cards) > 21:
#     print("You loose")
#     print("Dealer Win")

player_win_status=False
choice = 'y'

def black_jack_checker(player_cards,dealer_cards,player_win_status,choice):
    while choice == "y":
        if sum(player_cards) > 21:
            print(f"{player_cards} sum = {sum(player_cards)}")
            player_win_status = False
            return player_win_status

        if sum(dealer_cards) > 21:
            player_win_status = True
            return player_win_status
        choice = input("Do you want to withdraw another card 'y' or type 'n'").lower()
        if choice == 'n':
            if sum(player_cards) <= 21 and sum(dealer_cards) <= 21:
                if 21 - sum(player_cards) < 21 - sum(dealer_cards):
                    print(f"{player_cards} sum = {sum(player_cards)}")
                    player_win_status = True
                    return player_win_status
                elif 21 - sum(player_cards) > 21 - sum(dealer_cards):
                    print(f"{player_cards} sum = {sum(player_cards)}")
                    player_win_status = False
                    return player_win_status
                return player_win_status
            return player_win_status
        elif choice == 'y':
            player_cards.append(cards[random.randint(0, 12)])
            print(f"{player_cards} sum = {sum(player_cards)}")
            dealer_cards.append(cards[random.randint(0, 12)])







if black_jack_checker(player_cards,dealer_cards,player_win_status,choice):
    print(f"dealer card {dealer_cards}the sum of = {sum(dealer_cards)}")
    print(f"player cards {player_cards}the sum = {sum(player_cards)}")
    print ("You win")

else:
    print(f"dealer card {dealer_cards}the sum of = {sum(dealer_cards)}")
    print(f"player cards {player_cards}the sum = {sum(player_cards)}")
    print("You loose")




