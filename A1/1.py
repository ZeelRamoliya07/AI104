# (a) Generate a list with values from 0 to 49
list_a = list(range(50))
print(list_a)
print("\n")

# (b) Generate a list with the squares of numbers from 1 to 50
list_b = [(i + 1)**2 for i in range(50)]
print(list_b)
print("\n")

# (c) Generate a list of repeated characters
list_c = [chr(i + 97) * (i + 1) for i in range(26)]
print(list_c)
print("\n")
