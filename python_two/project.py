#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

import random
import sys


# Two useful variables for creating Cards.
SUITS = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        self.cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.cards.append(rank + suit)
        random.shuffle(self.cards)

    
    def shuffle(self):
        random.shuffle(self.cards)


    def halve(self):
        half = int(len(self.cards)/2)
        halfList = []
        for i in range(half):
            halfList.append(self.cards.pop(i))
        return (halfList, self.cards)
    

    def __str__(self):
        return str(self.cards)


    def __len__(self):
        return len(self.cards)


class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self, card_list):
        self.cards = card_list


    def add_card(self, new_card):
        self.cards.append(new_card)


    def rem_card(self):
        return self.cards.pop(0)



        
class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, hand, name):
        self.hand = hand
        self.name = name


    def play(self):
        return hand.rem_card()
        

    def count_cards(self):
        return len(self.hand)

def round_check(user_card, comp_card):
    """
    Fn: checks who won the battle/war
    Arg: 2 strings representing each card
    Ret: a tuple with a win code and both cards
    *** Win Code:
        0 - Player Wins
        1 - Computer Wins
        2 - Draw
    """
    print('User: {}\nComp: {}'.format(user_card, comp_card))
    if RANKS.index(user_card[:-1]) > RANKS.index(comp_card[:-1]):
        print('Player takes the round')
        return (0 , user_card, comp_card)
    elif RANKS.index(user_card[:-1]) < RANKS.index(comp_card[:-1]):
        print('Computer takes this one')
        return (1, user_card, comp_card)
    else:
        print('Draw. Prepare for the War!')
        return (2, user_card, comp_card)


def get_usr_round(name):
    """
    Fn: gets user input and performs basic sanitation
    Arg: name as a string
    Ret: choice in form of a char p, c, or q
    """
    choice = input('{}, do you want to [P]lay,'.format(name)
                    + '[C]heck number of cards, '
                    + 'or [Q]uit\neg. type "P" to play\n')
    while choice.upper() not in ['P', 'C', 'Q']:
        choice = input('Invalid selection; please type "P", "C", or "Q".')
    return choice.upper()


######################
#### GAME PLAY #######
######################
def game():
    print("Welcome to War, let's begin...")
    name = input('what is your name?\n')
    deck = Deck();
    usr_half, cmp_half = deck.halve()
    usr_half = Hand(usr_half)
    cmp_half = Hand(cmp_half)
    player = Player(usr_half, name)
    while True:
        choice = get_usr_round(name)
        if choice == 'P':
            pool = []
            code = 999
            while code not in [0,1]:
                code, card1, card2 = round_check(usr_half.rem_card(),
                                                cmp_half.rem_card())
                if code == 0:
                    usr_half.add_card(card1)
                    usr_half.add_card(card2)
                    if len(pool) != 0:
                            usr_half.extend(pool)
                elif code == 1:
                    cmp_half.add_card(card1)
                    cmp_half.add_card(card2)
                    if len(pool) != 0:
                        usr_half.extend(pool)
                elif code == 2:
                    pool.append(card1)
                    pool.append(card2)
                    for i in range(3):
                        pool.append(usr_half.rem_card())
                        pool.append(cmp_half.rem_card())
                    code, card1, card2 = round_check(
                                                    usr_half.rem_card(),
                                                    cmp_half.rem_card())
        elif choice == 'C':
            print(player.count_cards())
        else:
            sys.exit()
        if len(usr_half) == 0:
            print("{} has lost.".format(player.name))
            sys.exit()
        elif len(cmp_half) == 0:
            print("{} has won!".format(player.name))


game()              
