import random

points_for_player1=0
points_for_player2=0

print("This is a simulated card game called War, between 2 players")
player1=input("Player 1, please enter your name")
player2=input("Player 2, please enter your name")

basic_deck = list(range(2, 15)) * 4
random.shuffle(basic_deck)

def player_turn(turn):
    card = None
    if turn==1:
        print("\nIt is " + player1 + "'s turn")
        print(player1 + " drew card " + str(basic_deck[0]))
        card=basic_deck[0]
        basic_deck.pop(0)
    else:
        print("\nIt is " + player2 + "'s turn")
        print(player2 + " drew card " + str(basic_deck[0]))
        card=basic_deck[0]
        basic_deck.pop(0)
    return card

def compare_scores(card1, card2):
    global points_for_player1, points_for_player2
    if card1>card2:
        print(player1 + " had the higher card, so they get a point")
        points_for_player1+=1
    elif card1<card2:
        print(player2 + " had the higher card, so they get a point")
        points_for_player2+=1
    else:
         print(player1 + " and " + player2 + " had cards cards of equivalent value, so no one gets a point.")       

while basic_deck!=[]:
    card1 = player_turn(1)
    card2 = player_turn(2)
    compare_scores(card1, card2)
    
if points_for_player1>points_for_player2:
    print("\n" + player1 + " won, because he/she had the most points")
elif points_for_player1<points_for_player2:
    print("\n" + player2 + " won, because he/she had the most points")
else:
    print("\nIt ended as a tie, because " + player1 + " and " + player2 + " ended with the same score")

tie=26-(points_for_player1+points_for_player2)
print(player1 + " won " + str(points_for_player1) + " times.")
print(player2 + " won " + str(points_for_player2) + " times")
print(player1 + " and " + player2 + " tied " + str(tie) + " times")
