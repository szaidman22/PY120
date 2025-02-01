import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def play(self):
        self.number = random.randint(self.low, self.high)

        guesses_remaining = int(math.log2(self.high - self.low + 1)) + 1

        keep_going = True

        while keep_going and guesses_remaining > 0:
            print(f"You have {guesses_remaining} guesses remaining.")
            keep_going = self.round()
            guesses_remaining -= 1
        
        if keep_going:
            print(f"You have no more guesses. The number was {self.number} You lost!")

        if not keep_going:
            print("You won!\n")

    def round(self):
        lose = True
        guess = int(self.guess())

        while guess < self.low or guess > self.high:
            guess = int(self.guess_out_of_bounds())
        
        if guess < self.number:
            print("Your guess is too low.\n")

        if guess > self.number:
            print("Your guess is too high.\n")

        if guess == self.number:
            print("That's the number!\n")
            lose = False

        return lose

    def guess(self):
        return input(f"Enter a number between {self.low} and {self.high}: ")
    
    def guess_out_of_bounds(self):
        return input(f"Invalid guess. Enter a number between {self.low} and {self.high}: ")
    
game = GuessingGame(100, 1500)
game.play()