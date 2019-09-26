import random  # importing random function for generating random interger
from itertools import product
import Queue_linked_list  # importing cartesian product function from itertools

# Suit of cards
glob_suit = ("Clubs", "Diamonds", "Hearts", "Spades")
# Rank of cards
glob_rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

class Player:

    global glob_rank

    def __init__(self, Data):
        self.deck_of_cards = Data
        self.sort_cards()
        self.maintain_cards()
        self.print_deck()
        
    
    #def add_to_deck

    def sort_cards(self):#Sorting cards in a deck using bubble sort
        for j in range(0,(len(self.deck_of_cards))):
            for i in range(0,(len(self.deck_of_cards)-j-1)):
                interim = self.deck_of_cards[i]
                ex_interim = self.deck_of_cards[i+1]
                if (glob_rank.index(interim[1]) < glob_rank.index(ex_interim[1])):
                    temp = self.deck_of_cards[i]
                    self.deck_of_cards[i] = self.deck_of_cards[i+1]
                    self.deck_of_cards[i+1] = temp

    def maintain_cards(self):
        self.sort_cards()
        cards_in_hand = Queue_linked_list.Queue()
        for i in range(0,len(self.deck_of_cards)):
            cards_in_hand.en_queue(i)

    
    def print_deck(self):
        hand = Queue_linked_list.Queue()
        for q in self.deck_of_cards:
            hand.en_queue(q)
        hand.print_list()


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
    players=Queue_linked_list.Queue()
    for i in range(4):
        print("\nCards of player {} is :".format(i+1))
        player = Player(player_cards[i])
        players.en_queue(player)
        players.print_list()
        
                               
def main():
        deck_of_card()
  
    #for counter in range(0, 4):
        #print("cards of player", counter + 1, "->", cards[counter])


# Driver Function
if __name__=="__main__":
    main()
