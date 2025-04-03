"""
A magic square is an NxN grid of numbers in which the entries in each row, column and
main diagonal sum to the same number (equal to N(N^2+1)/2). Create a magic square for
N=4, 5, 6, 7, 8
"""

import numpy as np

def generate_odd_magic_square(n):
    magic_square = np.zeros((n, n), dtype=int)
    i, j = 0, n // 2  # Start position (first row, middle column)
    
    for num in range(1, n * n + 1):
        magic_square[i, j] = num
        new_i, new_j = (i - 1) % n, (j + 1) % n  # Move up-right
        if magic_square[new_i, new_j]:  # If occupied, move down instead
            i += 1
        else:
            i, j = new_i, new_j
    
    return magic_square

def generate_doubly_even_magic_square(n):
    magic_square = np.arange(1, n * n + 1).reshape(n, n)
    mask = np.zeros((n, n), dtype=bool)
    
    for i in range(n):
        for j in range(n):
            if (i % 4 == j % 4) or ((i % 4 + j % 4) == 3):  # Main diagonal conditions
                mask[i, j] = True
    
    magic_square[mask], magic_square[~mask] = magic_square[~mask], magic_square[mask]
    return magic_square

def generate_singly_even_magic_square(n):
    half_n = n // 2
    sub_square = generate_odd_magic_square(half_n)
    magic_square = np.zeros((n, n), dtype=int)
    
    # Copy small magic squares into four quadrants
    for i in range(2):
        for j in range(2):
            magic_square[i * half_n:(i + 1) * half_n, j * half_n:(j + 1) * half_n] = (
                sub_square + (i * 2 + j) * half_n * half_n
            )
    
    # Swap specific columns to balance the magic square
    k = (n - 2) // 4
    for i in range(half_n):
        for j in range(k):
            magic_square[i, j], magic_square[i + half_n, j] = (
                magic_square[i + half_n, j], magic_square[i, j]
            )
            magic_square[i, j + half_n + k], magic_square[i + half_n, j + half_n + k] = (
                magic_square[i + half_n, j + half_n + k], magic_square[i, j + half_n + k]
            )
    
    return magic_square

def generate_magic_square(n):
    if n % 2 == 1:
        return generate_odd_magic_square(n)
    elif n % 4 == 0:
        return generate_doubly_even_magic_square(n)
    else:
        return generate_singly_even_magic_square(n)

# Generate and print magic squares for N = 4, 5, 6, 7, 8
sizes = [4, 5, 6, 7, 8]
for size in sizes:
    print(f"Magic Square for N={size}:")
    print(generate_magic_square(size))
    print("\n")