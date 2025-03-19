# Function: FindDigits
def FindDigits(num):
    count = 0
    string = str(num)
    for i in range(len(string)):
        if int(string[i]) != 0 and num % int(string[i]) == 0:
            count += 1
    return count

# Input Number of Test Cases
N = int(input())

# Empty List to store all Test Cases
T = [0]*N

# Input Test Cases
for i in range(N):
    T[i] = input()

# Output the result  
for i in range(N):
    print(FindDigits(int(T[i])))
    
    
    
