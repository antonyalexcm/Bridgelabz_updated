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
    print(list_cards)
    return


def main():
    deck_of_card()
    #for counter in range(0, 4):
        #print("cards of player", counter + 1, "->", cards[counter])


if __name__=="__main__":
    main()
    