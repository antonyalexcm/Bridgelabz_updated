import random  # importing random function for generating random interger
from itertools import product  # importing cartesian product function from itertools


# function to produce deck of cards
def deck_of_card():
    # Suit of cards
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]  
    # Rank of cards
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    cartesian_product = product(suit,rank)
    list_cards = list(cartesian_product)
    random.shuffle(list_cards)
    distribute_card(list_cards) 
    return

def distribute_card(list_cards):
        #distributed_cards = []
        players = []
        counter = 0
        for j in range(4):
                new_list = []
                for k in range(9):
                        new_list.append(list_cards[counter])
                        counter += 1
                players.append(new_list)
        print_card(players)
        return

def print_card(player_cards):
        for i in range(1,5):
                print("\nThe cards received by player {} are : ".format(i))
                print(player_cards[(i-1)])
        return
                         
                        
def main():
        deck_of_card()
    #for counter in range(0, 4):
        #print("cards of player", counter + 1, "->", cards[counter])


# Driver Function
if __name__=="__main__":
    main()