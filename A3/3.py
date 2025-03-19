"""
                                    UTOPIAN TREE
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the
monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height
increases by 1 meter.
Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find
the height of the tree after N growth cycles?
Input Format
The first line contains an integer, T, the number of test cases.
T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.
Constraints
1 <= T <= 10
0 <= N <= 60
Output Format
For each test case, print the height of the Utopian tree after N cycles.
"""

def UtopianTree(num):
    height = 1
    for i in range(num):
        # If i is even, double the height (Monsoon)
        if i % 2 == 0: 
            height *= 2

        # If i is odd, add 1 to the height (Summer)
        else:
            height += 1

    return height

# Number of test cases
T = int(input())

List = []

for i in range(T):
    num = int(input())
    List.append(num)
    
for i in List:
    print(UtopianTree(i))

