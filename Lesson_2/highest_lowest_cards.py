#Update this class so you can use it to determine the 
# lowest ranking and highest ranking cards in a list of Card objects:

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


"""
For this exercise, numeric cards are low cards, ordered from 2 through 10. 
Jacks are higher than 10s, Queens are higher than Jacks, Kings are higher than Queens, 
and Aces are higher than Kings. The suit plays no part in the relative ranking of cards.

If you have two or more cards of the same rank in your list, your min and max methods 
should return one of the matching cards; it doesn't matter which one.

Besides any methods needed to determine the lowest and highest cards, 
create a __str__ method that returns a string representation of the card, e.g., 
"Jack of Diamonds", "4 of Clubs", etc.
"""

cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True