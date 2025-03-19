# Sherlock & Squares

def isSquare(num1,num2):
    count = 0

    for i in range(num1,num2+1):
        if i**0.5 == int(i**0.5): # Check if the square root of i is an integer
            count += 1
    
    return count


T = int(input())
listI = [] # List to store the initial values
listF = [] # List to store the final values

for i in range(T):
    N = input().split() # Read the initial and final values
    
    listI.append(N[0]) # Append the initial value to the list
    listF.append(N[1]) # Append the final value to the list

for i in range(T):
    print(isSquare(int(listI[i]),int(listF[i])))  # Output the result for each test case


