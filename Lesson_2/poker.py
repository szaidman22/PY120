# Include Card and Deck classes from the last two exercises.
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
                    standing = 11
                case "Queen":
                    standing = 12
                case "King":
                    standing = 13
                case "Ace":
                    standing = 14
    
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
    
class PokerHand:
    def __init__(self, deck):
        self.hand = []
        for _ in range(5):
            self.hand.append(deck.draw())

        self.all_suits = set(card.suit for card in self.hand)
        self.all_ranks = set(card.rank for card in self.hand)
        self.all_standings = set(card.get_standing() for card in self.hand)
        self.rank_counts = [[card.rank for card in self.hand].count(rank) for rank in self.all_ranks]

    def __str__(self):
        return '\n'.join([str(card) for card in self.hand])

    def print(self):
       print('\n'.join([str(card) for card in self.hand]))

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        return len(self.all_suits) == 1 and \
               len(self.all_standings) == 5 and \
               min(self.all_standings) == 10 and \
               max(self.all_standings) == 14

    def _is_straight_flush(self):
        return len(self.all_suits) == 1 and \
               len(self.all_standings) == 5 and \
               min(self.all_standings) == max(self.all_standings) - 4

    def _is_four_of_a_kind(self):
        return 4 in self.rank_counts
               
    def _is_full_house(self):
        return 3 in self.rank_counts and 2 in self.rank_counts

    def _is_flush(self):
        return len(self.all_suits) == 1 and \
               len(self.all_standings) == 5 and \
               min(self.all_standings) != max(self.all_standings) - 4

    def _is_straight(self):
        return len(self.all_suits) != 1 and \
               len(self.all_standings) == 5 and \
               min(self.all_standings) == max(self.all_standings) - 4

    def _is_three_of_a_kind(self):
        return 3 in self.rank_counts and \
               len(self.all_ranks) == 3

    def _is_two_pair(self):
        return self.rank_counts.count(2) == 2

    def _is_pair(self):
        return max(self.rank_counts) == 2

class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards


# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards


hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()