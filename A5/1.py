"""
1. Maximizing XOR
Given two integers: L and R, Find the maximal values of A xor B given, L <= A <= B <= R
Input Format:
The input contains two lines, L is present in the first line. R in the second line.
Constraints
1 <= L <= R <= 103
Output Format:
The maximal value as mentioned in the problem statement.

Sample Input #00:
1
10

Sample Output #00:
15

Sample Input #01:
10
15

Sample Output #01:
7
"""   

L = int(input())
R = int(input())

max = 0

for i in range(L,R+1):
    for j in range(L,R+1):
        if (i ^ j) > max:
            max = (i ^ j)

print(max)