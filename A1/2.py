import random

max0 = 0
list = [0] * 100

list0 = []

# Fill list with random 0's and 1's
for i in range(100):
    num = random.randint(0, 1)
    list[i] = num

# Count consecutive 0's
for i in range(100):
    if list[i] == 0:
        max0 += 1
    elif list[i] == 1:
        list0.append(max0)
        max0 = 0

# Output the list and max consecutive 0's
print(list)
print("\nMaximum consecutive 0's:", max(list0))
