T = int(input())

while(T!=0):
    NXS = input().split()

    N = int(NXS[0])
    X = int(NXS[1])
    S = int(NXS[2])

    A = [0]*S
    B = [0]*S
    
    coin = X
    
    for i in range(0,S):
        AB = input().split()
        A[i] = int(AB[0])
        B[i] = int(AB[1])
        
        if(coin == A[i]):
            coin = B[i]
        elif(coin == B[i]):
            coin = A[i] 
        else:
           pass       
           
    print(coin)
    T -= 1
