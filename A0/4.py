# User Input
a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))

# Display two numbers before swap
print("Before swapping")
print("Value of a :",a)
print("Value of b :",b)

# Swap Logic
a = a ^ b
b = a ^ b
a = a ^ b

# Display two numbers after swap
print("\nAfter swapping")
print("Value of a :",a)
print("Value of b :",b)