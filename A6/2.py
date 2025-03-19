"""
Write a class called Rock_paper_scissors that implements the logic of the game Rock paper-
scissors. For this game the user plays against the computer for a certain number of rounds.
Your class should have fields for the how many rounds there will be, the current round 
number, and the number of wins each player has. There should be methods for getting the 
computer’s choice, finding the winner of a round, and checking to see if someone has one 
the (entire) game. You may want more methods.
"""

import random

class RockPaperScissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['rock', 'paper', 'scissors']

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Draw"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_wins += 1
            return "User Wins"
        else:
            self.computer_wins += 1
            return "Computer Wins"

    def play_game(self):
        while self.current_round <= self.rounds:
            print(f"\nRound {self.current_round}:")
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in self.choices:
                print("Invalid choice, try again.")
                continue
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            self.current_round += 1
        
        print("\nFinal Results:")
        print(f"User Wins: {self.user_wins}, Computer Wins: {self.computer_wins}")
        if self.user_wins > self.computer_wins:
            print("Congratulations! You won the game.")
        elif self.user_wins < self.computer_wins:
            print("Computer wins! Better luck next time.")
        else:
            print("It's a tie!")

def rock_paper_scissors_menu():
    rounds = int(input("Enter number of rounds: "))
    game = RockPaperScissors(rounds)
    game.play_game()


rock_paper_scissors_menu()

