"""
1. Consider the 8 queen's problem, it is a 8*8 chess board where you need to place queens
according to the following constraints.
a. Each row should have exactly only one queen.
b. Each column should have exactly only one queen.
c. No queens are attacking each other.

Write a program to place the queens randomly in the chess board so that all the conditions
are satisfied. Find the solutions to the problem.
"""

import random

def is_valid(board):
    n = len(board)
    
    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) == abs(i - j):
                return False
    return True

def generate_valid_board():
    n = 8
    board = list(range(n))   
    while True:
        random.shuffle(board)
        if is_valid(board):
            return board

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ["-" for _ in range(n)]
        line[board[row]] = "Q" 
        print(" ".join(line))
    print("\n")

solution = generate_valid_board()
print("One Valid Solution:")
print_board(solution)