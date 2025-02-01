"""
Nouns: Player, Move, Rule
Verbs: Choose, Compare

Player:
- Choose

Move:
Rule:

- Compare

"""

class Player:
    def __init__(self):
        pass

    def choose():
        pass

class move:
    def __init__(self):
        pass

class rule:
    def __init__(self):
        pass

    def compare(self, move1, move2):
        pass

""" Orchestration engine class: where program flow goes, RPSGame
    - will need to be able to play it, so need play method """

class RPSGame:
    def __init__(self):
        self._human = Player()
        self._computer = Player()
    
    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def play(self):
        self._display_welcome_message()
        self._human.choose()
        self._computer.choose()
        display_winner()
        self._display_goodbye_message()
