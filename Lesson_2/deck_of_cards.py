# Using the Card class from the previous exercise, 
# create a Deck class that contains all of the standard 
# 52 playing cards. Use the following code to start your work:
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __gt__(self, other):
        return self.get_standing() > other.get_standing()
    
    def __lt__(self, other):
        return self.get_standing() < other.get_standing()
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
        
    def get_standing(self):
        if self.rank in range(1,11):
            standing = self.rank
        
        else:
            match self.rank:
                case "Jack":
                    standing = 12
                case "Queen":
                    standing = 13
                case "King":
                    standing = 14
                case "Ace":
                    standing = 15
    
        return standing
    
class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Deck.RANKS for suit in Deck.SUITS]
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.__init__()

        return self.cards.pop()
    
# The Deck class should provide a draw method to deal one card. 
# The Deck should be shuffled when it is initialized. If no more 
# cards remain when draw is called, the method should generate a 
# new set of 52 shuffled cards, then deal one card from the new cards.

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).