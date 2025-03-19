# Function to calculate factorial of number
def factorial(n):
    fact = 1

    if num < 0:
        print("Invalid input")

    elif num == 0:
        return 1

    else:

        for i in range(1,n+1):
            fact *= i
            i = i + 1
        return fact

# __main__

# User input
num = int(input("Enter any number to calculate its factorial : "))

print("The factorial of the given number is : ",factorial(num))
