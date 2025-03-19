"""
3. Bigger is Greater
Given a word w, rearrange the letters of w to construct another word s in such a way that s is
lexicographically greater than w.
Input Format:
The first line of inputs contains t, number of test cases. Each of the next t lines contains w.
Constraints:
1 <= t <= 105
1 <= |w| <= 100
w will contain only lower-case English letters and its length will not exceed 100.
Output Format:
For each test case, output a string lexicographically bigger than w in a separate line. In case of
multiple possible answers print the lexicographically smallest one and if no answer exists, print
no answer.
Sample Input:
3
ab
bb
hefg
Sample Output:
ba
no answer
hegf
"""

def biggerIsGreater(w):
    w = list(w)  # Convert string to list for mutability
    n = len(w)

    # Step 1: Find the pivot (first decreasing element from the right)
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1

    if i == -1:  # If no pivot found, return "no answer"
        return "no answer"

    # Step 2: Find the smallest character on the right of pivot that is greater than pivot
    j = n - 1
    while w[j] <= w[i]:
        j -= 1

    # Step 3: Swap pivot and the found character
    w[i], w[j] = w[j], w[i]

    # Step 4: Reverse the suffix (everything after i)
    w[i + 1:] = reversed(w[i + 1:])

    return "".join(w)  # Convert list back to string

t = int(input())

list = []

for i in range(t):
    w = input()
    list.append(w)

for i in list:
    print(biggerIsGreater(i))




