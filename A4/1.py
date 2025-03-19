# The Love-Letter Mystery

def isPalindrome(s):
    return s == s[::-1]

def getcount(string):
    count = 0
    # Convert string into a list for easier manipulation
    string = list(string)
    
    # Check if the string is already a palindrome
    if isPalindrome(string):
        return count

    n = len(string)
    
    # Iterate from the start of the string to the middle
    for i in range(n // 2):
        left = string[i]
        right = string[n - 1 - i]
        
        # If characters at position i and (n-i-1) are different, reduce the larger one
        while left != right:
            if ord(left) > ord(right):
                string[i] = chr(ord(left) - 1)  # Reduce left
                left = string[i]  # Update left with the modified character
            else:
                string[n - 1 - i] = chr(ord(right) - 1)  # Reduce right
                right = string[n - 1 - i]  # Update right with the modified character
            count += 1  # Increment the count for each operation
    
    return count

# Input handling
T = int(input())  # Read number of test cases
list_strings = []

for i in range(T):
    N = input()
    list_strings.append(N)

# Process each string and output the result
for s in list_strings:
    print(getcount(s))

    