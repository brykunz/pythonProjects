from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []
game_over = False

"""
make a list for player cards
make a list for dealer cards

make a draw function that takes a random value from cards[] and adds it to your hand list or dealer list

show player hand
ask if they want to hit or stay
only be showing one dealer card during this time

if you bust game over
if you pass the dealer flips their next card

The goal of blackjack is to get closer to 21 than the dealer without going over. 
If the dealer's total goes over 21, all players with a total of 21 or less win. 
 
If the game is tied, it's called a "push" and the bet is returned.
"""

def deal_hand(hand):
    hand.append(random.choice(cards))
    hand.append(random.choice(cards))
    print(hand)
    return hand

def deal_card(hand):
    hand.append(random.choice(cards))
    print(hand)
    return hand

def hand_math(hand):
    score = 0
    for dealt_cards in hand:
        score += dealt_cards
        if score > 21:
            if 11 in hand:
                hand.remove(11)
                hand.append(1)
                score -= 10
    return score

# def hand_math(hand):
#     score = 0
#     if hand == player_hand:
#         for dealt_cards in player_hand:
#             score += dealt_cards
#             if score > 21:
#                 if 11 in hand:
#                     hand.remove(11)
#                     hand.append(1)
#                     score -= 10
#         return score
#     else:
#         if hand == dealer_hand:
#             for dealt_cards in dealer_hand:
#                 score += dealt_cards
#                 if score > 21:
#                     if 11 in hand:
#                         hand.remove(11)
#                         hand.append(1)
#                         score -= 10
#             return score
                #check list for any 11's, then swap one of them to value 1
                #do dealer math
def hit_or_stay():
    hit = input("Do you HIT or STAY\n").lower()
    if hit == "hit":
        return True
    elif hit == "stay":
        return False
    else:
        print("Typo, try again.")
        hit_or_stay()

print(logo)
while not game_over:
    continue_hand = True

    player_hand.clear()
    dealer_hand.clear()

    deal_hand(player_hand)
    print(f"Player Score: {hand_math(player_hand)}")
    deal_card(dealer_hand)
    print(f"Dealer Score: {hand_math(dealer_hand)}")

    player_turn = hit_or_stay()

    while continue_hand:

        while player_turn:
            deal_card(player_hand)
            if hand_math(player_hand) > 21:
                print(f"Player Score: {hand_math(player_hand)}")
                print("You bust. Game over.")
                player_turn = False
                continue_hand = False
                game_over = True
            else:
                print(f"Player Score: {hand_math(player_hand)}")
                print(f"Dealer Score: {hand_math(dealer_hand)}")
                player_turn = hit_or_stay()
                continue_hand = True
                game_over = False

        if hand_math(dealer_hand) < 17:
            deal_card(dealer_hand)
            print(f"Dealer Score: {hand_math(dealer_hand)}")
        else:
            continue_hand = False

    print(f"Final Score:\n"
          f"Player Score: {hand_math(player_hand)}\n"
          f"Dealer Score: {hand_math(dealer_hand)}")
    if 21 >= hand_math(player_hand) and hand_math(player_hand) == hand_math(dealer_hand):
        print("Push.\n")
    elif 21 >= hand_math(dealer_hand) > hand_math(player_hand):
        print("Dealer wins!\n")
    else:
        print("You win!\n")

    if input("Do you want to play again? yes or no\n").lower() == "no":
        game_over = True