N = int(input())

for _ in range(N) :
    
    N_list = list(map(int, input().split()))
    N_list.sort()
    M = int(input())
    M_list = list(map(int, input().split()))
    
    for i in M_list :
        if i in N_list :
            print(1)
        else :
            print(0)
        
    # left = 0
    # right = N
    # mid = (left + right) // 2
    
    # if 